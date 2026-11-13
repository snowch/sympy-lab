// Copyright © 2026 Christopher Snow
import {escapeText} from './rich-text.mjs';
export function areaModelSvg(model,width=560){
 if(model?.kind!=='square-area'||!Number.isInteger(model.offset)||model.offset<1||model.offset>6)return '';
 const a=model.offset,v=escapeText(model.variable),side=Math.min(width-112,220),left=(width-side)/2,top=42;
 const split=side*3/(3+a),small=side-split,mid=left+split;
 const label=(x,y,t)=>`<text x="${x}" y="${y}" text-anchor="middle" dominant-baseline="middle">${t}</text>`;
 const cross=a===1?v:a+v;
 return `<svg xmlns="http://www.w3.org/2000/svg" class="area-model" viewBox="0 0 ${width} ${side+90}" role="img" aria-label="A square of side ${v} plus ${a}, split into ${v} squared, two rectangles of area ${cross}, and a corner of area ${a*a}."><style>.area-model text{font-family:system-ui,sans-serif;font-size:20px;fill:var(--ink,#15372c)}.area-model .large{fill:var(--diagram-one,#d9eee4)}.area-model .cross{fill:var(--diagram-two,#f3deb9)}.area-model .corner{fill:var(--diagram-three,#e4e8f8)}.area-model rect{stroke:var(--surface,#fff);stroke-width:2}</style><rect class="large" x="${left}" y="${top}" width="${split}" height="${split}"/><rect class="cross" x="${mid}" y="${top}" width="${small}" height="${split}"/><rect class="cross" x="${left}" y="${top+split}" width="${split}" height="${small}"/><rect class="corner" x="${mid}" y="${top+split}" width="${small}" height="${small}"/>${label(left+split/2,top+split/2,v+'²')}${label(mid+small/2,top+split/2,cross)}${label(left+split/2,top+split+small/2,cross)}${label(mid+small/2,top+split+small/2,String(a*a))}${label(left+split/2,22,v)}${label(mid+small/2,22,String(a))}${label(left-24,top+split/2,v)}${label(left-24,top+split+small/2,String(a))}</svg>`;
}
