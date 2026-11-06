# Warhammer 40k · Habilidades de narrativa

Kit de **10 skills de Story Skills** para historias extensas, personajes autónomos, causalidad, continuidad y prosa natural. Adaptado mediante reglas editoriales locales; no contiene los capítulos privados del proyecto.

**Aviso:** este repositorio se reutilizó a petición de su propietario. Conserva provisionalmente el nombre `ml-dog-cat-detection-yolo` porque el conector disponible no permite renombrarlo. Los archivos antiguos de YOLO ya no aparecen en la rama `main`, pero pueden recuperarse desde el historial de Git.

## Qué contiene

- `.agents/skills/`: **10 skills completas** (`SKILL.md` y sus referencias).
- `.claude/skills/`: entradas para Claude Code que leen el contenido anterior.
- `.gemini/skills/`: entradas para Gemini CLI que leen el contenido anterior.
- `AGENTS.md`, `CLAUDE.md` y `GEMINI.md`: instrucciones de acceso.
- `docs/REGLAS-NARRATIVAS.md`: criterios del proyecto y aprobación.
- `docs/USO.md`: compatibilidad, pruebas y limitaciones.
- `docs/ORIGEN.md`: versión y licencia de los archivos originales.

## Skills incluidas

1. `character-management`
2. `worldbuilding`
3. `plot-structure`
4. `research`
5. `discovery-drafting`
6. `scene-craft`
7. `voice-style`
8. `revision-continuity`
9. `line-editing`
10. `story-maintenance`

## Cómo comenzar

1. Abrir la copia local de este repositorio en un agente compatible (Codex, Claude Code o Gemini CLI).
2. Leer `docs/REGLAS-NARRATIVAS.md` y la skill relevante. Estas herramientas **no aprueban ni publican** automáticamente capítulos.
3. Primero realizar una **auditoría sin modificaciones** de un capítulo en una copia de pruebas: continuidad, naturalidad, evolución y agencia de personajes.
4. Si se necesitan verificaciones automáticas, revisar e instalar el **CLI oficial** por separado: `npm install -g story-skills`; este repositorio conserva instrucciones pero no el binario distribuido.

Agregar archivos al GitHub **no instala skills automáticamente** en las interfaces web de ChatGPT, Claude ni Gemini. Allí se debe importar una habilidad o adjuntar sus documentos según las funciones disponibles en la cuenta.

**Licencia:** [MIT de Story Skills](LICENSE-STORY-SKILLS) · [Fuente](https://github.com/danjdewhurst/story-skills).
