// Sprite d'icônes (traits 1.8, 24×24) — insérées une fois par page puis appelées via <use href="#i-…">
const I = {
  phone: '<path d="M6.6 3.5h3l1.5 3.8-2 1.3a12 12 0 0 0 5.3 5.3l1.3-2 3.8 1.5v3a1.9 1.9 0 0 1-2.1 1.9C10.6 17.6 6.4 13.4 4.7 5.6A1.9 1.9 0 0 1 6.6 3.5z"/>',
  mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
  clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 1.9"/>',
  pin: '<path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
  check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
  arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>',
  caret: '<polyline points="6 9 12 15 18 9"/>',
  hood: '<path d="M4 17h16l-3.5-6h-9z"/><path d="M10 11V4h4v7"/><path d="M8 20c1-1 2 1 3 0s2 1 3 0 2 1 3 0"/>',
  duct: '<path d="M4 20V10h8V4h8"/><path d="M8 20V14h8V8h4"/><path d="M12 4v4M4 14h4"/>',
  fan: '<circle cx="12" cy="12" r="2"/><path d="M12 10c0-4 1-7 4-7 2 0 2.5 3-4 7zM14 12c4 0 7 1 7 4 0 2-3 2.5-7-4zM12 14c0 4-1 7-4 7-2 0-2.5-3 4-7zM10 12c-4 0-7-1-7-4 0-2 3-2.5 7 4z"/>',
  filter: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 4l-2 16M11 4l-2 16M15 4l-2 16M19 4l-2 16"/>',
  layers: '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
  doc: '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/><circle cx="16.5" cy="17" r="1.6"/>',
  calendar: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18M8 14h2M12 14h2M8 17h2"/>',
  search: '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
  home: '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
  kitchen: '<rect x="3" y="11" width="18" height="10" rx="1"/><path d="M3 15h18M7 11V8M12 11V6M17 11V8"/><circle cx="7.5" cy="18" r=".6"/><circle cx="16.5" cy="18" r=".6"/>',
  refresh: '<path d="M20 11a8 8 0 0 0-14.7-4.3L3 9"/><path d="M3 4v5h5"/><path d="M4 13a8 8 0 0 0 14.7 4.3L21 15"/><path d="M21 20v-5h-5"/>',
  sparkle: '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
  fire: '<path d="M12 21c4 0 7-2.7 7-6.5 0-4-3.5-6-4-10-2.5 1.5-4 4-4 6.5-1-1-1.5-2-1.5-3.5C7 9.2 5 11.7 5 14.5 5 18.3 8 21 12 21z"/>',
  flame: '<path d="M12 3c1 3 4 4.5 4 8a4 4 0 0 1-8 0c0-1.7.8-2.8 1.6-3.6.2 1.4.9 2.1 1.9 2.4C11 7.5 11 5 12 3z"/><path d="M4 21h16"/><path d="M6 18h12"/>',
  snow: '<path d="M12 2v20M4.9 6l14.2 12M19.1 6L4.9 18"/><path d="M9 4l3 2 3-2M9 20l3-2 3 2"/>',
  shield: '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
  badge: '<circle cx="12" cy="9" r="6"/><path d="M8.5 13.9L7 22l5-3 5 3-1.5-8.1"/><path d="M9.5 9l1.8 1.8L14.8 7.5"/>',
  users: '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2a5 5 0 0 1 5.5 5"/>',
  info: '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 7.8v.2"/>',
  alert: '<path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17v.2"/>',
  star: '<path d="M12 3l2.8 5.8 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.3l1.1-6.2L3 9.7l6.2-.9z"/>',
  plate: '<circle cx="12" cy="13" r="7"/><circle cx="12" cy="13" r="3.5"/><path d="M3 3v6M21 3v18M3 6h2"/>',
  burger: '<path d="M4 11a8 6 0 0 1 16 0z"/><path d="M3 14h18M4 17h16a0 0 0 0 1 0 0 2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/>',
  pizza: '<path d="M12 21L3.5 5.5A15 15 0 0 1 20.5 5.5z"/><circle cx="10" cy="9" r="1"/><circle cx="14" cy="10" r="1"/><circle cx="12" cy="14" r="1"/>',
  wok: '<path d="M3 11h18a9 6 0 0 1-18 0z"/><path d="M21 11l2-1M9 5c0-1 1-1 1-2M13 5c0-1 1-1 1-2"/>',
  bread: '<path d="M4 12a4 4 0 0 1 3-6h10a4 4 0 0 1 3 6v7H4z"/><path d="M9 10l1 2M13 10l1 2"/>',
  building: '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1M10 21v-3h4v3"/>',
  heart: '<path d="M12 20s-7.5-4.5-7.5-10A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 7.5 3c0 5.5-7.5 10-7.5 10z"/><path d="M8 12h2l1-2 2 4 1-2h2"/>',
  box: '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
  chef: '<path d="M7 14a4 4 0 0 1-1-7.8A4.5 4.5 0 0 1 12 4a4.5 4.5 0 0 1 6 2.2A4 4 0 0 1 17 14"/><path d="M7 14v6h10v-6"/><path d="M7 17h10"/>',
  truck: '<path d="M2 6h12v10H2zM14 9h4l3 4v3h-7z"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
  map: '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
  graduation: '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/><path d="M22 9v6"/>',
  ladder: '<path d="M7 3v18M17 3v18M7 7h10M7 12h10M7 17h10"/>',
  flask: '<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7 15h10"/>',
  cross: '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>',
  bolt: '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
  camera: '<path d="M4 7h3l2-3h6l2 3h3a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="4"/>',
  moon: '<path d="M20 14.5A8 8 0 1 1 9.5 4 6.5 6.5 0 0 0 20 14.5z"/>',
  euro: '<path d="M17 6a7 7 0 1 0 0 12"/><path d="M4 10h9M4 14h9"/>',
  menu: '<path d="M4 7h16M4 12h16M4 17h16"/>',
  close: '<path d="M6 6l12 12M18 6L6 18"/>'
};
export const iconNames = Object.keys(I);
export const sprite =
  '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">' +
  Object.entries(I).map(([k, v]) => `<symbol id="i-${k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${v}</symbol>`).join("") +
  "</svg>";
export const ico = (name, cls = "ico") => `<svg class="${cls}" aria-hidden="true"><use href="#i-${name}"/></svg>`;
export const logo = `<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#0e1c2b"/><rect x="21" y="7" width="6" height="13" rx="1" fill="#9fb1c3"/><path d="M11 31h26l-6-11H17z" fill="#e0701b"/><path d="M11 31h26" stroke="#ffb070" stroke-width="2"/><path d="M15 38c2-2.2 3.5 2.2 5.5 0s3.5 2.2 5.5 0 3.5 2.2 5.5 0" fill="none" stroke="#5fd39c" stroke-width="2.2" stroke-linecap="round"/></svg>`;
