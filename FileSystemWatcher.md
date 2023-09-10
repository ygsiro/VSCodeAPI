# FileSystemWatcher

A file system watcher notifies about changes to files and folders on disk or from other FileSystemProviders.

To get an instance of a FileSystemWatcher use createFileSystemWatcher.

## Events

### onDidChange

```typescript
onDidChange: Event<Uri>
```

### onDidCreate

```typescript
onDidCreate: Event<Uri>
```

### onDidDelete

```typescript
onDidDelete: Event<Uri>
```

## Properties

### ignoreChangeEvents

```typescript
ignoreChangeEvents: boolean
```

### ignoreCreateEvents

```typescript
ignoreCreateEvents: boolean
```

### ignoreDeleteEvents

```typescript
ignoreDeleteEvents: boolean
```

## Methods

### dispose

```typescript
dispose(): any
```

[Event]: EventT.md
[Uri]: Uri.md
