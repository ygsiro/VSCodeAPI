# TextDocument

Represents a text document, such as a source file. Text documents have lines and knowledge about an underlying resource like a file.

## Properties

### eol

```typescript
eol: EndOfLine
```

### fileName

```typescript
fileName: string
```

### isClosed

```typescript
isClosed: boolean
```

### isDirty

```typescript
isDirty: boolean
```

### isUntitled

```typescript
isUntitled: boolean
```

### languageId

```typescript
languageId: string
```

### lineCount

```typescript
lineCount: number
```

### uri

```typescript
uri: Uri
```

### version

```typescript
version: number
```

## Methods

### getText

```typescript
getText(range?: Range): string
```

### getWordRangeAtPosition

```typescript
getWordRangeAtPosition(position: Position, regex?: RegExp): Range
```

### lineAt

```typescript
//1)
lineAt(line: number): TextLine
//2)
lineAt(position: Position): TextLine
```

### offsetAt

```typescript
offsetAt(position: Position): number
```

### positionAt

```typescript
positionAt(offset: number): Position
```

### save

```typescript
save(): Thenable<boolean>
```

### validatePosition

```typescript
validatePosition(position: Position): Position
```

### validateRange

```typescript
validateRange(range: Range): Range
```

