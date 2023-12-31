# WebviewPanel

A panel that contains a webview.

## Events

### onDidChangeViewState

```typescript
onDidChangeViewState: Event<WebviewPanelOnDidChangeViewStateEvent>
```

Fired when the panel's view state changes.

### onDidDispose

```typescript
onDidDispose: Event<void>
```

Fired when the panel is disposed.

This may be because the user closed the panel or because `.dispose()` was called on it.

Trying to use the panel after it after it has been disposed throws an exception.

## Properties

### active

```typescript
active: boolean
```

Whether the panel is active (focused by the user).

### iconPath

```typescript
iconPath?: Uri | {dark: Uri, light: Uri}
```

Icon for the panel shown in UI.

### options

```typescript
options: WebviewPanelOptions
```

Content settings for the webview panel.

### title

```typescript
title: string
```

Title of the panel shown in UI.

### viewColumn

```typescript
viewColumn: ViewColumn
```

Editor position of the panel.
This property is only set if the webview is in one of the editor view columns.

### viewType

```typescript
viewType: string
```

Identifies the type of the webview panel, such as `markdown.preview`.

### visible

```typescript
visible: boolean
```

Whether the panel is visible.

### webview

```typescript
webview: Webview
```

[Webview] belonging to the panel.

## Methods

### dispose

```typescript
dispose(): any
```

Dispose of the webview panel.

This closes the panel if it showing and disposes of the resources owned by the webview.
Webview panels are also disposed when the user closes the webview panel.
Both cases fire the `onDispose` event.

**Returns**

+ any

### reveal

```typescript
reveal(viewColumn?: ViewColumn, preserveFocus?: boolean): void
```

Show the webview panel in a given column.

A webview panel may only show in a single column at a time.
If it is already showing, this method moves it to new column.

**Parameter**

+ *viewColumn*?: [ViewColumn]
  + View column to show the panel in.
    Shows in the current `viewColumn` if undefined.
+ *preserveFocus*?: boolean
  + When `true`, the webview will not take focus.

**Returns**

+ void

[WebviewPanelOnDidChangeViewStateEvent]: WebviewPanelOnDidChangeViewStateEvent.md
[Uri]: Uri.md
[ViewColumn]: ViewColumn.md
[Webview]: Webview.md
[WebviewPanelOptions]: WebviewPanelOptions.md
[Event]: EventT.md
