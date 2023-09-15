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

Event fired when the view is disposed.

Views are disposed when they are explicitly hidden by a user
(this happens when a user right clicks in a view and unchecks the webview view).

Trying to use the view after it has been disposed throws an exception.

## Properties

### badge

```typescript
badge?: ViewBadge
```

The badge to display for this webview view.
To remove the badge, set to undefined.

### description

```typescript
description?: string
```

Human-readable string which is rendered less prominently in the title.

### title

```typescript
title?: string
```

View title displayed in the UI.

The view title is initially taken from the extension `package.json` contribution.

### viewType

```typescript
viewType: string
```

Identifies the type of the webview view, such as `hexEditor.dataView`.

### visible

```typescript
visible: boolean
```

Tracks if the webview is currently visible.

Views are visible when they are on the screen and expanded.

### webview

```typescript
webview: Webview
```

The underlying webview for the view.

## Methods

### show

```typescript
show(preserveFocus?: boolean): void
```

Reveal the view in the UI.

If the view is collapsed, this will expand it.

**Parameter**

+ *preserveFocus*?: boolean
  + When `true` the view will not take focus.

[Event]: EventT.md
[Webview]: Webview.md
[ViewBadge]: ViewBadge.md
