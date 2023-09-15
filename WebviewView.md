# WebviewView

A webview based view.

## Events

### onDidChangeVisibility

```typescript
onDidChangeVisibility: Event<void>
```

Event fired when the visibility of the view changes.

Actions that trigger a visibility change:

+ The view is collapsed or expanded.
+ The use switches to a different view group in the sidebar or panel.

Note that hiding a view using the context menu instead disposes of the view and fires `onDidDispose`

### onDidDispose

```typescript
onDidDispose: Event<void>
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

### title

```typescript
title?: string
```

### viewType

```typescript
viewType: string
```

### visible

```typescript
visible: boolean
```

### webview

```typescript
webview: Webview
```

## Methods

### show

```typescript
show(preserveFocus?: boolean): void
```

[Event]: EventT.md
[Webview]: Webview.md
[ViewBadge]: ViewBadge.md
