# WorkspaceConfiguration

Represents the configuration. It is a merged view of

Default Settings
Global (User) Settings
Workspace settings
Workspace Folder settings - From one of the Workspace Folders under which requested resource belongs to.
Language settings - Settings defined under requested language.
The effective value (returned by get) is computed by overriding or merging the values in the following order:

defaultValue (if defined in package.json otherwise derived from the value's type)
globalValue (if defined)
workspaceValue (if defined)
workspaceFolderValue (if defined)
defaultLanguageValue (if defined)
globalLanguageValue (if defined)
workspaceLanguageValue (if defined)
workspaceFolderLanguageValue (if defined)
Note: Only object value types are merged and all other value types are overridden.

Example 1: Overriding

```typescript
defaultValue = 'on';
globalValue = 'relative';
workspaceFolderValue = 'off';
value = 'off';
Example 2: Language Values

defaultValue = 'on';
globalValue = 'relative';
workspaceFolderValue = 'off';
globalLanguageValue = 'on';
value = 'on';
Example 3: Object Values

defaultValue = { a: 1, b: 2 };
globalValue = { b: 3, c: 4 };
value = { a: 1, b: 3, c: 4 };
Note: Workspace and Workspace Folder configurations contains launch and tasks settings. Their basename will be part of the section identifier. The following snippets shows how to retrieve all configurations from launch.json:

// launch.json configuration
const config = workspace.getConfiguration(
  'launch',
  vscode.workspace.workspaceFolders[0].uri
);

// retrieve values
const values = config.get('configurations');
Refer to Settings for more information.
```

## Methods

### get

```typescript
get<T>(section: string): T
```

### get

```typescript
get<T>(section: string, defaultValue: T): T
```

### has

```typescript
has(section: string): boolean
```

### inspect

```typescript
inspect<T>(section: string): {defaultLanguageValue: T, defaultValue: T, globalLanguageValue: T, globalValue: T, key: string, languageIds: string[], workspaceFolderLanguageValue: T, workspaceFolderValue: T, workspaceLanguageValue: T, workspaceValue: T}
```

### update

```typescript
update(section: string, value: any, configurationTarget?: boolean | ConfigurationTarget, overrideInLanguage?: boolean): Thenable<void>
```

[ConfigurationTarget]: ConfigurationTarget.md
[workspace]: workspace.md
[tasks]: tasks.md
