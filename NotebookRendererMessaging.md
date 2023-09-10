# NotebookRendererMessaging

Renderer messaging is used to communicate with a single renderer. It's returned from createRendererMessaging.

## Events

### onDidReceiveMessage

```typescript
onDidReceiveMessage: Event<{editor: NotebookEditor, message: any}>
```

## Methods

### postMessage

```typescript
postMessage(message: any, editor?: NotebookEditor): Thenable<boolean>
```

[Event]: EventT.md
[NotebookEditor]: NotebookEditor.md
