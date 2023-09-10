# extensions

Namespace for dealing with installed extensions. Extensions are represented by an Extension-interface which enables reflection on them.

Extension writers can provide APIs to other extensions by returning their API public surface from the activate-call.

```typescript
export function activate(context: vscode.ExtensionContext) {
  let api = {
    sum(a, b) {
      return a + b;
    },
    mul(a, b) {
      return a * b;
    }
  };
  // 'export' public api-surface
  return api;
}
```

When depending on the API of another extension add an extensionDependencies-entry to package.json, and use the getExtension-function and the exports-property, like below:

```typescript
let mathExt = extensions.getExtension('genius.math');
let importedApi = mathExt.exports;

console.log(importedApi.mul(42, 1));
```

## Variables

### all

```typescript
all: readonly Extension<any>[]
```

## Events

### onDidChange

```typescript
onDidChange: Event<void>
```

## Functions

### getExtension

```typescript
getExtension<T>(extensionId: string): Extension<T> | undefined
```

[Extension]: ExtensionT.md
[ExtensionContext]: ExtensionContext.md
[Event]: EventT.md
