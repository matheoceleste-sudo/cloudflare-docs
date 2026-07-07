import { useEffect, useRef, type HTMLAttributes } from "react";
import { cn } from "~/util/cn";

type DottedSurfaceProps = HTMLAttributes<HTMLDivElement>;

/**
 * Animated field of dots rendered on a 2D canvas.
 *
 * A dependency-free port of the popular `DottedSurface` component (the
 * original relies on three.js). It projects a grid of points through a
 * simple tilted perspective camera and animates them with a travelling
 * sine wave. Dot colour follows the container's `currentColor`, so it
 * adapts to light/dark themes automatically. Honours
 * `prefers-reduced-motion` by rendering a single static frame.
 */
export function DottedSurface({
	className,
	children,
	...props
}: DottedSurfaceProps) {
	const containerRef = useRef<HTMLDivElement>(null);
	const canvasRef = useRef<HTMLCanvasElement>(null);

	useEffect(() => {
		const container = containerRef.current;
		const canvas = canvasRef.current;
		if (!container || !canvas) return;

		const ctx = canvas.getContext("2d");
		if (!ctx) return;

		const SEPARATION = 60;
		const AMOUNTX = 50;
		const AMOUNTY = 50;
		const TILT = 0.5; // viewing angle in radians
		const FOCAL = 700;
		const CAM_Z = 1400;

		const prefersReducedMotion = window.matchMedia(
			"(prefers-reduced-motion: reduce)",
		).matches;

		let width = 0;
		let height = 0;
		let dpr = 1;
		let color = "rgba(255,255,255,";

		const readColor = () => {
			const computed = getComputedStyle(container).color;
			// Convert `rgb(r, g, b)` / `rgba(r, g, b, a)` into an `rgba(r,g,b,`
			// prefix so we can append a per-dot alpha value.
			const match = computed.match(/(\d+),\s*(\d+),\s*(\d+)/);
			color = match
				? `rgba(${match[1]},${match[2]},${match[3]},`
				: "rgba(255,255,255,";
		};

		const resize = () => {
			dpr = Math.min(window.devicePixelRatio || 1, 2);
			width = container.clientWidth;
			height = container.clientHeight;
			canvas.width = Math.max(1, Math.floor(width * dpr));
			canvas.height = Math.max(1, Math.floor(height * dpr));
			canvas.style.width = `${width}px`;
			canvas.style.height = `${height}px`;
			ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
			readColor();
		};

		resize();

		let count = 0;
		let animationId = 0;

		const render = () => {
			ctx.clearRect(0, 0, width, height);
			const centerX = width / 2;
			const centerY = height / 2;
			const cosTilt = Math.cos(TILT);
			const sinTilt = Math.sin(TILT);

			for (let ix = 0; ix < AMOUNTX; ix++) {
				for (let iy = 0; iy < AMOUNTY; iy++) {
					const wx = ix * SEPARATION - (AMOUNTX * SEPARATION) / 2;
					const wz = iy * SEPARATION - (AMOUNTY * SEPARATION) / 2;
					const wy =
						Math.sin((ix + count) * 0.3) * 30 +
						Math.sin((iy + count) * 0.5) * 30;

					// Rotate around the X axis, then perspective-project.
					const cy = wy * cosTilt - wz * sinTilt;
					const cz = wy * sinTilt + wz * cosTilt + CAM_Z;
					if (cz <= 1) continue;

					const scale = FOCAL / cz;
					const sx = centerX + wx * scale;
					const sy = centerY + cy * scale;

					const radius = Math.max(0.4, scale * 1.6);
					const wave =
						(Math.sin((ix + count) * 0.3) + 1) * 0.25 +
						(Math.sin((iy + count) * 0.5) + 1) * 0.25;
					const alpha = Math.min(0.9, Math.max(0.05, wave * scale * 1.4));

					ctx.beginPath();
					ctx.fillStyle = `${color}${alpha.toFixed(3)})`;
					ctx.arc(sx, sy, radius, 0, Math.PI * 2);
					ctx.fill();
				}
			}
		};

		const animate = () => {
			count += 0.1;
			render();
			animationId = requestAnimationFrame(animate);
		};

		if (prefersReducedMotion) {
			render();
		} else {
			animationId = requestAnimationFrame(animate);
		}

		const resizeObserver = new ResizeObserver(() => {
			resize();
			if (prefersReducedMotion) render();
		});
		resizeObserver.observe(container);

		return () => {
			cancelAnimationFrame(animationId);
			resizeObserver.disconnect();
		};
	}, []);

	return (
		<div ref={containerRef} className={cn("relative", className)} {...props}>
			<canvas
				ref={canvasRef}
				aria-hidden="true"
				className="pointer-events-none absolute inset-0 h-full w-full"
			/>
			{children}
		</div>
	);
}

export default DottedSurface;
