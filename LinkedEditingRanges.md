# LinkedEditingRanges

Represents a list of ranges that can be edited together along with a word pattern to describe valid range contents.

## Constructors

```typescript
new LinkedEditingRanges(ranges: Range[], wordPattern?: RegExp): LinkedEditingRanges
```

## Properties

### ranges

```typescript
ranges: Range[]
```

### wordPattern

```typescript
wordPattern: RegExp
```

## Location

### Represents

```typescript
Represents a location inside a resource, such as a line inside a text file.
```

## Constructors

```typescript
new Location(uri: Uri, rangeOrPosition: Range | Position): Location
```

## Properties

### range

```typescript
range: Range
```

### uri

```typescript
uri: Uri
```

[Range]: Range.md
[Position]: Position.md
[Uri]: Uri.md
