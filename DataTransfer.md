# DataTransfer

A map containing a mapping of the mime type of the corresponding transferred data.

Drag and drop controllers that implement handleDrag can add additional mime types to the data transfer. These additional mime types will only be included in the handleDrop when the the drag was initiated from an element in the same drag and drop controller.

## Constructors

```typescript
new DataTransfer(): DataTransfer
```

## Methods

### [iterator](): IterableIterator<[mimeType: string, item: DataTransferItem]>

```typescript
[iterator](): IterableIterator<[mimeType: string, item: DataTransferItem]>
```

### forEach

```typescript
forEach(callbackfn: (item: DataTransferItem, mimeType: string, dataTransfer: DataTransfer) => void, thisArg?: any): void
```

### get

```typescript
get(mimeType: string): DataTransferItem
```

### set

```typescript
set(mimeType: string, value: DataTransferItem): void
```

