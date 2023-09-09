# workspace

Namespace for dealing with the current workspace. A workspace is the collection of one or more folders that are opened in an editor window (instance).

It is also possible to open an editor without a workspace. For example, when you open a new editor window by selecting a file from your platform's File menu, you will not be inside a workspace. In this mode, some of the editor's capabilities are reduced but you can still open text files and edit them.

Refer to https://code.visualstudio.com/docs/editor/workspaces for more information on the concept of workspaces.

The workspace offers support for listening to fs events and for finding files. Both perform well and run outside the editor-process so that they should be always used instead of nodejs-equivalents.

## Variables

### fs

```typescript
fs: FileSystem
```

### isTrusted

```typescript
isTrusted: boolean
```

### name

```typescript
name: string | undefined
```

### notebookDocuments

```typescript
notebookDocuments: readonly NotebookDocument[]
```

### rootPath

```typescript
rootPath: string | undefined
```

### textDocuments

```typescript
textDocuments: readonly TextDocument[]
```

### workspaceFile

```typescript
workspaceFile: Uri | undefined
```

### workspaceFolders

```typescript
workspaceFolders: readonly WorkspaceFolder[] | undefined
```

## Events

### onDidChangeConfiguration

```typescript
onDidChangeConfiguration: Event<ConfigurationChangeEvent>
```

### onDidChangeNotebookDocument

```typescript
onDidChangeNotebookDocument: Event<NotebookDocumentChangeEvent>
```

### onDidChangeTextDocument

```typescript
onDidChangeTextDocument: Event<TextDocumentChangeEvent>
```

### onDidChangeWorkspaceFolders

```typescript
onDidChangeWorkspaceFolders: Event<WorkspaceFoldersChangeEvent>
```

### onDidCloseNotebookDocument

```typescript
onDidCloseNotebookDocument: Event<NotebookDocument>
```

### onDidCloseTextDocument

```typescript
onDidCloseTextDocument: Event<TextDocument>
```

### onDidCreateFiles

```typescript
onDidCreateFiles: Event<FileCreateEvent>
```

### onDidDeleteFiles

```typescript
onDidDeleteFiles: Event<FileDeleteEvent>
```

### onDidGrantWorkspaceTrust

```typescript
onDidGrantWorkspaceTrust: Event<void>
```

### onDidOpenNotebookDocument

```typescript
onDidOpenNotebookDocument: Event<NotebookDocument>
```

### onDidOpenTextDocument

```typescript
onDidOpenTextDocument: Event<TextDocument>
```

### onDidRenameFiles

```typescript
onDidRenameFiles: Event<FileRenameEvent>
```

### onDidSaveNotebookDocument

```typescript
onDidSaveNotebookDocument: Event<NotebookDocument>
```

### onDidSaveTextDocument

```typescript
onDidSaveTextDocument: Event<TextDocument>
```

### onWillCreateFiles

```typescript
onWillCreateFiles: Event<FileWillCreateEvent>
```

### onWillDeleteFiles

```typescript
onWillDeleteFiles: Event<FileWillDeleteEvent>
```

### onWillRenameFiles

```typescript
onWillRenameFiles: Event<FileWillRenameEvent>
```

### onWillSaveNotebookDocument

```typescript
onWillSaveNotebookDocument: Event<NotebookDocumentWillSaveEvent>
```

### onWillSaveTextDocument

```typescript
onWillSaveTextDocument: Event<TextDocumentWillSaveEvent>
```

## Functions

### applyEdit

```typescript
applyEdit(edit: WorkspaceEdit, metadata?: WorkspaceEditMetadata): Thenable<boolean>
```

### asRelativePath

```typescript
asRelativePath(pathOrUri: string | Uri, includeWorkspaceFolder?: boolean): string
```

### createFileSystemWatcher

```typescript
createFileSystemWatcher(globPattern: GlobPattern, ignoreCreateEvents?: boolean, ignoreChangeEvents?: boolean, ignoreDeleteEvents?: boolean): FileSystemWatcher
```

### findFiles

```typescript
findFiles(include: GlobPattern, exclude?: GlobPattern, maxResults?: number, token?: CancellationToken): Thenable<Uri[]>
```

### getConfiguration

```typescript
getConfiguration(section?: string, scope?: ConfigurationScope): WorkspaceConfiguration
```

### getWorkspaceFolder

```typescript
getWorkspaceFolder(uri: Uri): WorkspaceFolder | undefined
```

### openNotebookDocument

```typescript
openNotebookDocument(uri: Uri): Thenable<NotebookDocument>
```

### openNotebookDocument

```typescript
openNotebookDocument(notebookType: string, content?: NotebookData): Thenable<NotebookDocument>
```

### openTextDocument

```typescript
openTextDocument(uri: Uri): Thenable<TextDocument>
```

### openTextDocument

```typescript
openTextDocument(fileName: string): Thenable<TextDocument>
```

### openTextDocument

```typescript
openTextDocument(options?: {content: string, language: string}): Thenable<TextDocument>
```

### registerFileSystemProvider

```typescript
registerFileSystemProvider(scheme: string, provider: FileSystemProvider, options?: {isCaseSensitive: boolean, isReadonly: boolean}): Disposable
```

### registerNotebookSerializer

```typescript
registerNotebookSerializer(notebookType: string, serializer: NotebookSerializer, options?: NotebookDocumentContentOptions): Disposable
```

### registerTaskProvider

```typescript
registerTaskProvider(type: string, provider: TaskProvider<Task>): Disposable
```

### registerTextDocumentContentProvider

```typescript
registerTextDocumentContentProvider(scheme: string, provider: TextDocumentContentProvider): Disposable
```

### saveAll

```typescript
saveAll(includeUntitled?: boolean): Thenable<boolean>
```

### updateWorkspaceFolders

```typescript
updateWorkspaceFolders(start: number, deleteCount: number, ...workspaceFoldersToAdd: {name: string, uri: Uri}[]): boolean
```

