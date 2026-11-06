# Uso, compatibilidad y verificación

## En el repositorio

- **Codex:** las skills reales están en `.agents/skills/<nombre>/SKILL.md`.
- **Claude Code:** las entradas en `.claude/skills/<nombre>/SKILL.md` indican dónde leer la skill real y sus referencias.
- **Gemini CLI:** los adaptadores de `.gemini/skills/<nombre>/SKILL.md` hacen lo mismo.

Estos adaptadores dependen de acceso de lectura a toda la carpeta del repositorio; deben probarse en cada instalación. No se ha probado su detección en el computador del usuario.

## Aplicaciones web

- **Claude.ai / Gemini web:** requieren importar skills individualmente con sus referencias, sujeto a las funciones y límites de cada cuenta. Tener un repositorio en GitHub no realiza esa importación.
- **ChatGPT Plus:** usar instrucciones y archivos en un Proyecto; no implica ejecución automática de scripts ni instalación nativa de skills.

## CLI de Story Skills

Las skills son instrucciones Markdown. Algunas describen comandos `story` que requieren **software adicional**. No se ha copiado `skills/story-maintenance/scripts/story.js`, un script distribuido de gran tamaño. Se puede instalar la versión oficial, tras revisar el paquete, desde una terminal de confianza:

```powershell
npm install -g story-skills
story --help
```

No ejecutar `story init`, `story import`, `reindex` ni `wordcount --write` sobre documentos originales sin copia de seguridad y autorización. Tampoco asumir que un PDF o un manuscrito existente ya usa el formato Story Skills.

## Prueba inicial recomendada

1. Preparar una copia del texto aprobado y sus documentos de contexto.
2. Auditar **sin escribir** con `scene-craft`, `revision-continuity`, `voice-style` y `character-management`.
3. Clasificar cada observación como evidencia confirmada, hipótesis o falso positivo.
4. Comparar las sugerencias con los objetivos editoriales y el canon.
5. Proponer cambios específicos; no aplicarlos hasta que se aprueben.

No se han ejecutado pruebas de integración locales de Claude Code, Codex o Gemini CLI.
