# TestItemCollection

Collection of test items, found in children and items.

## Properties

### size

```typescript
size: number
```

## Methods

### add

```typescript
add(item: TestItem): void
```

### delete

```typescript
delete(itemId: string): void
```

### forEach

```typescript
forEach(callback: (item: TestItem, collection: TestItemCollection) => unknown, thisArg?: any): void
```

### get

```typescript
get(itemId: string): TestItem
```

### replace

```typescript
replace(items: readonly TestItem[]): void
```

