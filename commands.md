# commands

Namespace for dealing with commands. In short, a command is a function with a unique identifier. The function is sometimes also called command handler.

Commands can be added to the editor using the registerCommand and registerTextEditorCommand functions. Commands can be executed manually or from a UI gesture. Those are:

palette - Use the commands-section in package.json to make a command show in the command palette.
keybinding - Use the keybindings-section in package.json to enable keybindings for your extension.
Commands from other extensions and from the editor itself are accessible to an extension. However, when invoking an editor command not all argument types are supported.

This is a sample that registers a command handler and adds an entry for that command to the palette. First register a command handler with the identifier extension.sayHello.

```typescript
commands.registerCommand('extension.sayHello', () => {
  window.showInformationMessage('Hello World!');
});
```

Second, bind the command identifier to a title under which it will show in the palette (package.json).

```json
{
  "contributes": {
    "commands": [
      {
        "command": "extension.sayHello",
        "title": "Hello World"
      }
    ]
  }
}
```

## Functions

### executeCommand

```typescript
executeCommand<T>(command: string, ...rest: any[]): Thenable<T>
```

### getCommands

```typescript
getCommands(filterInternal?: boolean): Thenable<string[]>
```

### registerCommand

```typescript
registerCommand(command: string, callback: (args: any[]) => any, thisArg?: any): Disposable
```

### registerTextEditorCommand

```typescript
registerTextEditorCommand(command: string, callback: (textEditor: TextEditor, edit: TextEditorEdit, args: any[]) => void, thisArg?: any): Disposable
```

