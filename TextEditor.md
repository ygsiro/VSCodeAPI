# TextEditor

Represents an editor that is attached to a document.

## Properties

### document

```typescript
document: TextDocument
```

### options

```typescript
options: TextEditorOptions
```

### selection

```typescript
selection: Selection
```

### selections

```typescript
selections: readonly Selection[]
```

### viewColumn

```typescript
viewColumn: ViewColumn
```

### visibleRanges

```typescript
visibleRanges: readonly Range[]
```

## Methods

### edit

```typescript
edit(callback: (editBuilder: TextEditorEdit) => void, options?: {undoStopAfter: boolean, undoStopBefore: boolean}): Thenable<boolean>
```

### hide

```typescript
hide(): void
```

### insertSnippet

```typescript
insertSnippet(snippet: SnippetString, location?: Range | Position | readonly Range[] | readonly Position[], options?: {undoStopAfter: boolean, undoStopBefore: boolean}): Thenable<boolean>
```

### revealRange

```typescript
revealRange(range: Range, revealType?: TextEditorRevealType): void
```

### setDecorations

```typescript
setDecorations(decorationType: TextEditorDecorationType, rangesOrOptions: readonly Range[] | readonly DecorationOptions[]): void
```

### show

```typescript
show(column?: ViewColumn): void
```

