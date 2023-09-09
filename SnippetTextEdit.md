# SnippetTextEdit

A snippet edit represents an interactive edit that is performed by the editor.

Note that a snippet edit can always be performed as a normal text edit. This will happen when no matching editor is open or when a workspace edit contains snippet edits for multiple files. In that case only those that match the active editor will be performed as snippet edits and the others as normal text edits.

## Static

### insert

```typescript
insert(position: Position, snippet: SnippetString): SnippetTextEdit
```

### replace

```typescript
replace(range: Range, snippet: SnippetString): SnippetTextEdit
```

## Constructors

```typescript
new SnippetTextEdit(range: Range, snippet: SnippetString): SnippetTextEdit
```

## Properties

### range

```typescript
range: Range
```

### snippet

```typescript
snippet: SnippetString
```

