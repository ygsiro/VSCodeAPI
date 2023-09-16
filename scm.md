# scm

## Variables

### inputBox

```typescript
inputBox: SourceControlInputBox
```

The input box for the last source control created by the extension.

+ *deprecated* - Use SourceControl.inputBox instead

## Functions

### createSourceControl

```typescript
createSourceControl(id: string, label: string, rootUri?: Uri): SourceControl
```

Creates a new source control instance.

**Parameter**

+ *id*: string
  + An `id` for the source control.
    Something short, e.g.: `git`.
+ *label*: string 
  + A human-readable string for the source control. E.g.: `Git`.
+ *rootUri*?: [Uri]
  + An optional Uri of the root of the source control. E.g.: `Uri.parse(workspaceRoot)`.

**Returns**

+ [SourceControl]
  + An instance of source control.

[Uri]: Uri.md
[SourceControl]: SourceControl.md
[SourceControlInputBox]: SourceControlInputBox.md
