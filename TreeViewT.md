# TreeView<T>

Represents a Tree view

## Events

### onDidChangeCheckboxState

```typescript
onDidChangeCheckboxState: Event<TreeCheckboxChangeEvent<T>>
```

### onDidChangeSelection

```typescript
onDidChangeSelection: Event<TreeViewSelectionChangeEvent<T>>
```

### onDidChangeVisibility

```typescript
onDidChangeVisibility: Event<TreeViewVisibilityChangeEvent>
```

### onDidCollapseElement

```typescript
onDidCollapseElement: Event<TreeViewExpansionEvent<T>>
```

### onDidExpandElement

```typescript
onDidExpandElement: Event<TreeViewExpansionEvent<T>>
```

## Properties

### badge

```typescript
badge?: ViewBadge
```

### description

```typescript
description?: string
```

### message

```typescript
message?: string
```

### selection

```typescript
selection: readonly T[]
```

### title

```typescript
title?: string
```

### visible

```typescript
visible: boolean
```

## Methods

### dispose

```typescript
dispose(): any
```

### reveal

```typescript
reveal(element: T, options?: {expand: number | boolean, focus: boolean, select: boolean}): Thenable<void>
```

