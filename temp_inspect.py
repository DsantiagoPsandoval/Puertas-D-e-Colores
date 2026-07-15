from pathlib import Path
p = Path('fundacion-puertas-de-colores (4).html').read_text(encoding='utf-8')
idx = p.index('div class="nos-photo-collage"')
print(repr(p[idx:idx+400]))
end = p.index('<!-- MVV FLIP CARDS -->', idx)
print('---')
print(repr(p[idx:end]))
