# TextEditorEdit

A complex edit that will be applied in one transaction on a TextEditor. This holds a description of the edits and if the edits are valid (i.e. no overlapping regions, document was not changed in the meantime, etc.) they can be applied on a document associated with a text editor.

## Methods

### delete

```typescript
delete(location: Range | Selection): void
```

### insert

```typescript
insert(location: Position, value: string): void
```

### replace

```typescript
replace(location: Range | Position | Selection, value: string): void
```

### setEndOfLine

```typescript
setEndOfLine(endOfLine: EndOfLine): void
```

[Selection]: Selection.md
[Range]: Range.md
[EndOfLine]: EndOfLine.md
[Position]: Position.md
