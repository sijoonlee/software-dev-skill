---
name: typescript-best-practices
description: Apply when reading, writing, or reviewing any .ts or .tsx file. TypeScript-specific rules for modeling state with discriminated unions, avoiding `as` and `any`, parsing external data with the repo's schema library, exhaustive switches, `satisfies`, derived types, and object arguments.
---

# TypeScript best practices

The **model-the-domain** skill says why. This skill is how to do it in TypeScript. When existing code follows a different convention, match the codebase.

## Model variants as discriminated unions

```ts
// Don't: contradictory states compile
type DiffState = { loading: boolean; diff?: GitDiff; error?: string };

// Do: only valid states exist
type DiffState =
	| { kind: 'loading' }
	| { kind: 'ready'; diff: GitDiff }
	| { kind: 'error'; error: string };
```

Pick one discriminant name (`kind`, `type`, or `status`) per codebase and keep it. If you can write a comment explaining which field combinations are valid, make it a union.

## Brand IDs that mean different things

```ts
type OrgId = string & { readonly __brand: 'OrgId' };
type UserId = string & { readonly __brand: 'UserId' };

function parseOrgId(input: string): OrgId {
	if (!input.startsWith('org_')) throw new Error(`Invalid org id: ${input}`);
	return input as OrgId; // the one allowed cast, right after the check
}
```

Validate once where the value enters. Downstream functions take `OrgId` and trust it.

## Make illegal values unconstructable, only where it pays

```ts
type NonEmpty<T> = [T, ...T[]];
const isNonEmpty = <T>(xs: T[]): xs is NonEmpty<T> => xs.length > 0;
```

Keep plain `T[]` while every operation on it works for empty input. Switch to `NonEmpty<T>` only where the loose type forces a `!`, a cast, or a "should never happen" throw.

## Parse external data, don't cast it

External data (HTTP bodies, JSON, env, database rows, `searchParams`) is `unknown` until parsed. Use the schema library the repo already has, and infer the type from the schema.

```ts
// Don't
const user = data as User;

// Do
const UserSchema = z.object({ id: z.string(), email: z.string().email() });
type User = z.infer<typeof UserSchema>;
const user = UserSchema.parse(data); // or safeParse when failure is a normal branch
```

- No `any`. Use `unknown` and narrow it.
- Don't hand-write a property-by-property type guard when a schema can do it.
- Parse once at the boundary. Don't re-validate deep in the call chain.

## Narrow in this order

1. A discriminant check (`switch (s.kind)`).
2. `'key' in obj`.
3. `typeof` or `instanceof`.
4. A type guard (`isX(value): value is X`) that really checks the claim. A guard that lies is worse than `as`, because its name says it's safe.
5. `as`, only after validation.

To remove an existing `as`, find why TypeScript can't infer the type. The usual fixes are adding a discriminant, narrowing a `Record<string, unknown>`, or parsing at the boundary.

## Make switches exhaustive

```ts
switch (state.kind) {
	case 'loading': return renderSpinner();
	case 'ready': return renderDiff(state.diff);
	case 'error': return renderError(state.error);
	default: {
		const _exhaustive: never = state;
		return _exhaustive;
	}
}
```

When someone adds a variant, the compiler points at every switch that needs a new case. A `Record<Union, X>` lookup table gives the same guarantee.

## Prefer `satisfies` to `as` for literals

```ts
const config = { theme: 'dark', cols: 3 } satisfies Config;
// checked against Config, and config.theme stays the literal 'dark'
```

## Derive types instead of redeclaring them

When a schema, generated client, or another type already defines a shape, derive from it with `Pick`, `Omit`, `Parameters`, `ReturnType`, `Awaited`, `typeof`, or `z.infer`. A hand-copied type drifts silently when the source changes.

## Pass an object when arguments can be swapped

```ts
// Don't: swapping two strings still compiles
createLeadPrice(partnerId, vertical, '2026-01-01', '2026-03-31');

// Do
createLeadPrice({ partnerId, vertical, startDate: '2026-01-01', endDate: '2026-03-31' });
```

Skip this on hot paths, such as per-frame render code or parsers, where the extra object matters.

## Logging

No `console.log` in shipped server code. Use the repo's structured logger with enough context to debug from an id, for example `logger.error('[dashboard] feature resolution failed', { error, organizationId })`.
