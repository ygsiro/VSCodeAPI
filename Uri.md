# Uri

A universal resource identifier representing either a file on disk or another resource, like untitled resources.

## Static

### file

```typescript
file(path: string): Uri
```

### from

```typescript
from(components: {authority: string, fragment: string, path: string, query: string, scheme: string}): Uri
```

### joinPath

```typescript
joinPath(base: Uri, ...pathSegments: string[]): Uri
```

### parse

```typescript
parse(value: string, strict?: boolean): Uri
```

## Constructors

```typescript
new Uri(scheme: string, authority: string, path: string, query: string, fragment: string): Uri
```

## Properties

### authority

```typescript
authority: string
```

### fragment

```typescript
fragment: string
```

### fsPath

```typescript
fsPath: string
```

### path

```typescript
path: string
```

### query

```typescript
query: string
```

### scheme

```typescript
scheme: string
```

## Methods

### toJSON

```typescript
toJSON(): any
```

### toString

```typescript
toString(skipEncoding?: boolean): string
```

### with

```typescript
with(change: {authority: string, fragment: string, path: string, query: string, scheme: string}): Uri
```

