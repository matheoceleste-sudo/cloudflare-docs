import { useEffect, useRef } from "react";
import { cn } from "~/util/cn";

interface HeroProps {
	trustBadge?: {
		text: string;
		icons?: string[];
	};
	headline?: {
		line1: string;
		line2: string;
	};
	subtitle?: string;
	buttons?: {
		primary?: {
			text: string;
			onClick?: () => void;
		};
		secondary?: {
			text: string;
			onClick?: () => void;
		};
	};
	className?: string;
}

const FRAGMENT_SHADER = `
precision highp float;
uniform float u_time;
uniform vec2 u_resolution;

void main() {
	vec2 uv = gl_FragCoord.xy / u_resolution.xy;
	vec2 p = uv * 2.0 - 1.0;
	p.x *= u_resolution.x / u_resolution.y;

	float t = u_time * 0.15;
	float v = 0.0;
	v += sin(p.x * 1.5 + t);
	v += sin((p.y + t) * 1.8);
	v += sin((p.x + p.y + t) * 1.2);
	v += sin(length(p) * 3.5 - t * 2.0);
	v *= 0.25;

	vec3 base = vec3(0.03, 0.03, 0.09);
	vec3 violet = vec3(0.35, 0.10, 0.65);
	vec3 blue = vec3(0.08, 0.28, 0.75);

	vec3 color = mix(base, violet, 0.5 + 0.5 * sin(v * 3.14159));
	color = mix(color, blue, 0.5 + 0.5 * cos(v * 3.14159 + t));

	// Vignette so the centre stays readable behind the text.
	float d = length(uv - 0.5);
	color *= smoothstep(0.95, 0.35, d) * 0.6 + 0.4;

	gl_FragColor = vec4(color, 1.0);
}
`;

const VERTEX_SHADER = `
attribute vec2 a_position;
void main() {
	gl_Position = vec4(a_position, 0.0, 1.0);
}
`;

/**
 * Full-screen hero with an animated WebGL shader background.
 *
 * Dependency-free port of the `animated-shader-hero` component: the
 * flowing gradient is a raw GLSL fragment shader on a full-screen quad
 * (no three.js). Falls back to a static CSS gradient when WebGL is
 * unavailable, and renders a single frame under
 * `prefers-reduced-motion`.
 */
export default function Hero({
	trustBadge,
	headline,
	subtitle,
	buttons,
	className,
}: HeroProps) {
	const canvasRef = useRef<HTMLCanvasElement>(null);

	useEffect(() => {
		const canvas = canvasRef.current;
		if (!canvas) return;

		const gl =
			(canvas.getContext("webgl") as WebGLRenderingContext | null) ??
			(canvas.getContext(
				"experimental-webgl",
			) as WebGLRenderingContext | null);

		if (!gl) {
			// Graceful fallback: a static gradient handled via CSS below.
			canvas.style.background =
				"radial-gradient(ellipse at center, #2a1a5e 0%, #0a0a18 70%)";
			return;
		}

		const compile = (type: number, source: string) => {
			const shader = gl.createShader(type);
			if (!shader) return null;
			gl.shaderSource(shader, source);
			gl.compileShader(shader);
			if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
				gl.deleteShader(shader);
				return null;
			}
			return shader;
		};

		const vertex = compile(gl.VERTEX_SHADER, VERTEX_SHADER);
		const fragment = compile(gl.FRAGMENT_SHADER, FRAGMENT_SHADER);
		if (!vertex || !fragment) return;

		const program = gl.createProgram();
		if (!program) return;
		gl.attachShader(program, vertex);
		gl.attachShader(program, fragment);
		gl.linkProgram(program);
		if (!gl.getProgramParameter(program, gl.LINK_STATUS)) return;
		gl.useProgram(program);

		// Full-screen triangle.
		const buffer = gl.createBuffer();
		gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
		gl.bufferData(
			gl.ARRAY_BUFFER,
			new Float32Array([-1, -1, 3, -1, -1, 3]),
			gl.STATIC_DRAW,
		);
		const positionLoc = gl.getAttribLocation(program, "a_position");
		gl.enableVertexAttribArray(positionLoc);
		gl.vertexAttribPointer(positionLoc, 2, gl.FLOAT, false, 0, 0);

		const timeLoc = gl.getUniformLocation(program, "u_time");
		const resolutionLoc = gl.getUniformLocation(program, "u_resolution");

		const resize = () => {
			const dpr = Math.min(window.devicePixelRatio || 1, 2);
			const width = canvas.clientWidth;
			const height = canvas.clientHeight;
			canvas.width = Math.max(1, Math.floor(width * dpr));
			canvas.height = Math.max(1, Math.floor(height * dpr));
			gl.viewport(0, 0, canvas.width, canvas.height);
			gl.uniform2f(resolutionLoc, canvas.width, canvas.height);
		};
		resize();

		const prefersReducedMotion = window.matchMedia(
			"(prefers-reduced-motion: reduce)",
		).matches;

		let animationId = 0;
		const start = performance.now();

		const render = (now: number) => {
			gl.uniform1f(timeLoc, (now - start) / 1000);
			gl.drawArrays(gl.TRIANGLES, 0, 3);
			animationId = requestAnimationFrame(render);
		};

		if (prefersReducedMotion) {
			gl.uniform1f(timeLoc, 0);
			gl.drawArrays(gl.TRIANGLES, 0, 3);
		} else {
			animationId = requestAnimationFrame(render);
		}

		const resizeObserver = new ResizeObserver(() => {
			resize();
			if (prefersReducedMotion) gl.drawArrays(gl.TRIANGLES, 0, 3);
		});
		resizeObserver.observe(canvas);

		return () => {
			cancelAnimationFrame(animationId);
			resizeObserver.disconnect();
			gl.deleteProgram(program);
			gl.deleteShader(vertex);
			gl.deleteShader(fragment);
			gl.deleteBuffer(buffer);
		};
	}, []);

	return (
		<section
			className={cn(
				"relative flex min-h-[100dvh] w-full items-center justify-center overflow-hidden bg-[#0a0a18]",
				className,
			)}
		>
			<canvas
				ref={canvasRef}
				aria-hidden="true"
				className="absolute inset-0 h-full w-full"
			/>

			<div className="relative z-10 mx-auto flex max-w-3xl flex-col items-center px-6 text-center">
				{trustBadge && (
					<div className="mb-8 inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/5 px-4 py-1.5 text-sm text-white/80 backdrop-blur-sm">
						{trustBadge.icons?.map((icon, index) => (
							<span key={index} aria-hidden="true">
								{icon}
							</span>
						))}
						<span>{trustBadge.text}</span>
					</div>
				)}

				{headline && (
					<h1 className="bg-gradient-to-b from-white to-white/60 bg-clip-text text-4xl font-bold leading-tight tracking-tight text-transparent sm:text-5xl md:text-6xl lg:text-7xl">
						{headline.line1}
						<br />
						{headline.line2}
					</h1>
				)}

				{subtitle && (
					<p className="mt-6 max-w-2xl text-base text-white/70 sm:text-lg">
						{subtitle}
					</p>
				)}

				{buttons && (buttons.primary || buttons.secondary) && (
					<div className="mt-10 flex flex-col items-center gap-4 sm:flex-row">
						{buttons.primary && (
							<button
								type="button"
								onClick={buttons.primary.onClick}
								className="rounded-full bg-white px-6 py-3 font-medium text-slate-950 transition-transform hover:scale-105"
							>
								{buttons.primary.text}
							</button>
						)}
						{buttons.secondary && (
							<button
								type="button"
								onClick={buttons.secondary.onClick}
								className="rounded-full border border-white/25 bg-white/5 px-6 py-3 font-medium text-white backdrop-blur-sm transition-colors hover:bg-white/10"
							>
								{buttons.secondary.text}
							</button>
						)}
					</div>
				)}
			</div>
		</section>
	);
}
