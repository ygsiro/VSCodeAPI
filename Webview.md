# Webview

Displays html content, similarly to an iframe.

## Events

### onDidReceiveMessage

```typescript
onDidReceiveMessage: Event<any>
```

## Properties

### cspSource

```typescript
cspSource: string
```

### html

```typescript
html: string
```

### options

```typescript
options: WebviewOptions
```

## Methods

### asWebviewUri

```typescript
asWebviewUri(localResource: Uri): Uri
```

### postMessage

```typescript
postMessage(message: any): Thenable<boolean>
```

