# ColorPresentation

A color presentation object describes how a Color should be represented as text and what edits are required to refer to it from source code.

For some languages one color can have multiple presentations, e.g. css can represent the color red with the constant Red, the hex-value #ff0000, or in rgba and hsla forms. In csharp other representations apply, e.g. System.Drawing.Color.Red.

## Constructors

```typescript
new ColorPresentation(label: string): ColorPresentation
```

## Properties

### additionalTextEdits

```typescript
additionalTextEdits?: TextEdit[]
```

### label

```typescript
label: string
```

### textEdit

```typescript
textEdit?: TextEdit
```

[TextEdit]: TextEdit.md
