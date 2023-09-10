# TestItem

An item shown in the "test explorer" view.

A TestItem can represent either a test suite or a test itself, since they both have similar capabilities.

## Properties

### busy

```typescript
busy: boolean
```

### canResolveChildren

```typescript
canResolveChildren: boolean
```

### children

```typescript
children: TestItemCollection
```

### description

```typescript
description?: string
```

### error

```typescript
error: string | MarkdownString
```

### id

```typescript
id: string
```

### label

```typescript
label: string
```

### parent

```typescript
parent: TestItem
```

### range

```typescript
range: Range
```

### sortText

```typescript
sortText?: string
```

### tags

```typescript
tags: readonly TestTag[]
```

### uri

```typescript
uri: Uri
```

[Range]: Range.md
[MarkdownString]: MarkdownString.md
[Uri]: Uri.md
[TestItemCollection]: TestItemCollection.md
[TestTag]: TestTag.md
