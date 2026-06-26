"use client";
import { useState, useRef, useCallback, useEffect } from "react";
import { cn } from "@/lib/utils";

interface BeforeAfterSliderProps {
  beforeSrc?: string;
  afterSrc?: string;
  beforeLabel?: string;
  afterLabel?: string;
  beforeBg?: string;
  afterBg?: string;
  aspectRatio?: string;
  className?: string;
}

export default function BeforeAfterSlider({
  beforeSrc,
  afterSrc,
  beforeLabel = "Avant",
  afterLabel  = "Après",
  beforeBg    = "from-slate-700 to-slate-900",
  afterBg     = "from-blue-100 to-blue-200",
  aspectRatio = "aspect-[16/9]",
  className,
}: BeforeAfterSliderProps) {
  const [position,  setPosition]  = useState(50);
  const [dragging,  setDragging]  = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  const updatePosition = useCallback((clientX: number) => {
    if (!containerRef.current) return;
    const { left, width } = containerRef.current.getBoundingClientRect();
    const pct = Math.min(Math.max(((clientX - left) / width) * 100, 2), 98);
    setPosition(pct);
  }, []);

  const onMouseDown = (e: React.MouseEvent) => { setDragging(true); updatePosition(e.clientX); };
  const onTouchStart = (e: React.TouchEvent) => { setDragging(true); updatePosition(e.touches[0].clientX); };

  useEffect(() => {
    if (!dragging) return;
    const onMove  = (e: MouseEvent)  => updatePosition(e.clientX);
    const onTouch = (e: TouchEvent)  => updatePosition(e.touches[0].clientX);
    const onUp    = ()               => setDragging(false);
    window.addEventListener("mousemove",  onMove);
    window.addEventListener("touchmove",  onTouch, { passive: true });
    window.addEventListener("mouseup",    onUp);
    window.addEventListener("touchend",   onUp);
    return () => {
      window.removeEventListener("mousemove",  onMove);
      window.removeEventListener("touchmove",  onTouch);
      window.removeEventListener("mouseup",    onUp);
      window.removeEventListener("touchend",   onUp);
    };
  }, [dragging, updatePosition]);

  return (
    <div
      ref={containerRef}
      className={cn("relative overflow-hidden rounded-xl select-none cursor-col-resize shadow-2xl", aspectRatio, className)}
      onMouseDown={onMouseDown}
      onTouchStart={onTouchStart}
      role="img"
      aria-label="Comparaison avant/après nettoyage"
    >
      {/* BEFORE (full width background) */}
      <div className="absolute inset-0">
        {beforeSrc ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={beforeSrc} alt={beforeLabel} className="w-full h-full object-cover" draggable={false} />
        ) : (
          <div className={cn("w-full h-full bg-gradient-to-br flex items-center justify-center", beforeBg)}>
            <div className="text-center text-white/50 pointer-events-none">
              <p className="text-xs uppercase tracking-widest font-semibold">Photo</p>
              <p className="text-sm mt-1">{beforeLabel}</p>
            </div>
          </div>
        )}
        {/* AVANT label */}
        <span className="absolute top-4 left-4 bg-black/60 text-white text-xs font-bold tracking-widest uppercase px-3 py-1.5 rounded backdrop-blur-sm">
          {beforeLabel}
        </span>
      </div>

      {/* AFTER (clipped overlay) */}
      <div
        className="absolute inset-0 overflow-hidden"
        style={{ clipPath: `inset(0 ${100 - position}% 0 0)` }}
      >
        {afterSrc ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={afterSrc} alt={afterLabel} className="w-full h-full object-cover" draggable={false} />
        ) : (
          <div className={cn("w-full h-full bg-gradient-to-br flex items-center justify-center", afterBg)}>
            <div className="text-center text-navy/50 pointer-events-none">
              <p className="text-xs uppercase tracking-widest font-semibold">Photo</p>
              <p className="text-sm mt-1">{afterLabel}</p>
            </div>
          </div>
        )}
        {/* APRÈS label */}
        <span className="absolute top-4 right-4 bg-gold/90 text-navy text-xs font-bold tracking-widest uppercase px-3 py-1.5 rounded backdrop-blur-sm">
          {afterLabel}
        </span>
      </div>

      {/* Divider line */}
      <div
        className="absolute inset-y-0 w-0.5 bg-white shadow-[0_0_12px_rgba(255,255,255,0.8)] pointer-events-none"
        style={{ left: `${position}%` }}
      />

      {/* Drag handle */}
      <div
        className="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 w-11 h-11 rounded-full bg-white shadow-xl flex items-center justify-center pointer-events-none z-10 border-2 border-gold"
        style={{ left: `${position}%` }}
      >
        <svg width="18" height="14" viewBox="0 0 18 14" fill="none">
          <path d="M1 7h16M1 7L4 4M1 7L4 10M17 7L14 4M17 7L14 10" stroke="#B8952A" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </div>
    </div>
  );
}
