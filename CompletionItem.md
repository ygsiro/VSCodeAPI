# CompletionItem

A completion item represents a text snippet that is proposed to complete text that is being typed.

It is sufficient to create a completion item from just a label. In that case the completion item will replace the word until the cursor with the given label or insertText. Otherwise the given edit is used.

When selecting a completion item in the editor its defined or synthesized text edit will be applied to all cursors/selections whereas additionalTextEdits will be applied as provided.

See also

provideCompletionItems
resolveCompletionItem

## Constructors

```typescript
new CompletionItem(label: string | CompletionItemLabel, kind?: CompletionItemKind): CompletionItem
```

## Properties

### additionalTextEdits

```typescript
additionalTextEdits?: TextEdit[]
```

### command

```typescript
command?: Command
```

### commitCharacters

```typescript
commitCharacters?: string[]
```

### detail

```typescript
detail?: string
```

### documentation

```typescript
documentation?: string | MarkdownString
```

### filterText

```typescript
filterText?: string
```

### insertText

```typescript
insertText?: string | SnippetString
```

### keepWhitespace

```typescript
keepWhitespace?: boolean
```

### kind

```typescript
kind?: CompletionItemKind
```

### label

```typescript
label: string | CompletionItemLabel
```

### preselect

```typescript
preselect?: boolean
```

### range

```typescript
range?: Range | {inserting: Range, replacing: Range}
```

### sortText

```typescript
sortText?: string
```

### tags

```typescript
tags?: readonly Deprecated[]
```

### textEdit

```typescript
textEdit?: TextEdit
```

