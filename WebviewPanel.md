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

### visible

```typescript
visible: boolean
```

### webview

```typescript
webview: Webview
```

## Methods

### dispose

```typescript
dispose(): any
```

### reveal

```typescript
reveal(viewColumn?: ViewColumn, preserveFocus?: boolean): void
```

[WebviewPanelOnDidChangeViewStateEvent]: WebviewPanelOnDidChangeViewStateEvent.md
[Uri]: Uri.md
[ViewColumn]: ViewColumn.md
[Webview]: Webview.md
[WebviewPanelOptions]: WebviewPanelOptions.md
[Event]: EventT.md
