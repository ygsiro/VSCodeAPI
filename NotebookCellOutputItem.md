# NotebookCellOutputItem

One representation of a notebook output, defined by MIME type and data.

## Static

### error

```typescript
error(value: Error): NotebookCellOutputItem
```

### json

```typescript
json(value: any, mime?: string): NotebookCellOutputItem
```

### stderr

```typescript
stderr(value: string): NotebookCellOutputItem
```

### stdout

```typescript
stdout(value: string): NotebookCellOutputItem
```

### text

```typescript
text(value: string, mime?: string): NotebookCellOutputItem
```

## Constructors

```typescript
new NotebookCellOutputItem(data: Uint8Array, mime: string): NotebookCellOutputItem
```

## Properties

### data

```typescript
data: Uint8Array
```

### mime

```typescript
mime: string
```

