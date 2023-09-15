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

## Properties

### active

```typescript
active: boolean
```

### iconPath

```typescript
iconPath?: Uri | {dark: Uri, light: Uri}
```

### options

```typescript
options: WebviewPanelOptions
```

### title

```typescript
title: string
```

### viewColumn

```typescript
viewColumn: ViewColumn
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
