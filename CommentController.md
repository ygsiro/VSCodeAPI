# CommentController

A comment controller is able to provide comments support to the editor and provide users various ways to interact with comments.

## Properties

### commentingRangeProvider

```typescript
commentingRangeProvider?: CommentingRangeProvider
```

### id

```typescript
id: string
```

### label

```typescript
label: string
```

### options

```typescript
options?: CommentOptions
```

### reactionHandler

```typescript
reactionHandler?: (comment: Comment, reaction: CommentReaction) => Thenable<void>
```

## Methods

### createCommentThread

```typescript
createCommentThread(uri: Uri, range: Range, comments: readonly Comment[]): CommentThread
```

### dispose

```typescript
dispose(): void
```

[Range]: Range.md
[comments]: comments.md
[Uri]: Uri.md
[CommentReaction]: CommentReaction.md
[Comment]: Comment.md
[CommentingRangeProvider]: CommentingRangeProvider.md
[CommentThread]: CommentThread.md
[CommentOptions]: CommentOptions.md
