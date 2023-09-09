## CodeActionProvider&lt;T&gt;

Provides contextual actions for code. Code actions typically either fix problems or beautify/refactor code.

Code actions are surfaced to users in a few different ways:

The lightbulb feature, which shows a list of code actions at the current cursor position. The lightbulb's list of actions includes both quick fixes and refactorings.
As commands that users can run, such as Refactor. Users can run these from the command palette or with keybindings.
As source actions, such Organize Imports.
Quick fixes are shown in the problems view.
Change applied on save by the editor.codeActionsOnSave setting.

## Methods

### provideCodeActions

```typescript
provideCodeActions(document: TextDocument, range: Range | Selection, context: CodeActionContext, token: CancellationToken): ProviderResult<Command | T[]>
```

### resolveCodeAction

```typescript
resolveCodeAction(codeAction: T, token: CancellationToken): ProviderResult<T>
```

