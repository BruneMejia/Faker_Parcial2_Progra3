## Repo: Faker_Parcial2_Progra3 — Copilot instructions

This repository is a small Python project (student assignment) that generates fake user data and displays it with a PyQt5 GUI. The guidance below helps an AI coding agent become productive quickly by focusing on discoverable patterns, run/debug steps, and realistic edit constraints.

High-level overview
- Purpose: generate fake users (names, emails, addresses) for El Salvador / Mexico and display them in a PyQt5 window.
- Key files: `Ejemplo1.py`, `Ejemplo2.py`, `Ejemplo3.py` (main exercises). `Ejemplo3.py` is the most complete: it defines a custom Faker provider `ElSalvadorProvider` and the `VentanaPrincipal` GUI.
- Dependencies: listed in `requirements.txt` (Faker, PyQt5, tzdata). Use the pinned versions there when adding or reproducing environment.

How to run and debug (developer workflows)
- Run locally (Windows/cmd.exe): install dependencies from `requirements.txt` then run the desired example. Typical commands in this repo use the system Python:

  python -m pip install -r requirements.txt
  python Ejemplo3.py

- GUI note: these scripts open a PyQt5 window and block the terminal until closed. For small edits, run the script interactively or add a `if __name__ == "__main__":` guard (already present in `Ejemplo3.py`).

Project-specific patterns and conventions
- Simple single-file exercises: each `EjemploN.py` contains a self-contained GUI app. Follow the existing pattern for UI composition: a QWidget subclass, layout in __init__, and a `generar` method that appends to a QTextEdit.
- Faker provider pattern: `Ejemplo3.py` adds a custom provider class `ElSalvadorProvider(BaseProvider)` with methods `departamento()`, `ciudad()`, `colonia()`, `direccion_completa()`. Use `fake.add_provider(ElSalvadorProvider)` to attach it to Faker instances.
- Normalization for emails: the code uses `unicodedata.normalize('NFKD', ...)` and filters combining characters to remove diacritics before building email addresses. Reuse `quitar_tildes()` when generating email-safe strings.
- Randomization: `random.randint` and `random.choice` are used to produce numeric suffixes and select domains. Preserve the small domain list `['gmail.com','hotmail.com']` unless adding tests that mock randomness.

Integration points and external dependencies
- Main external libraries: `Faker` and `PyQt5`. Avoid upgrading to major versions without verification; tests are manual (GUI-based). If adding CI later, prefer headless tests that mock Qt or run minimal logic separate from the UI.
- The custom provider is the principal cross-component integration point: code that needs a Salvadoran address should call `fake.direccion_completa()` after `fake.add_provider(ElSalvadorProvider)`.

Change guidance for contributors (what to modify and what not to change)
- Safe edits: adding unit-testable helper functions (e.g., email normalizer), refactoring the provider into a separate module, or parameterizing the number of generated users.
- Avoid: large refactors of the GUI framework (switching from PyQt5 to another toolkit) and changing pinned dependency versions in `requirements.txt` without testing the GUI runs locally.

Examples to reference when making edits
- To add a new field to the generated user, mimic the `generar_usuarios()` method in `Ejemplo3.py` (build fields, append to QTextEdit). Use `quitar_tildes()` for email-safe text.
- To add new address data, extend the `self.data` dict in `ElSalvadorProvider` and add a corresponding helper method if needed.

Testing and verification
- There are no automated tests in the repo. Quick manual verification steps:
  1) Install `requirements.txt` in a virtualenv.
  2) Run `python Ejemplo3.py` and click "Generar Usuarios".
  3) Confirm generated emails contain no diacritics and addresses follow a simple pattern with a street name, number, colonia, city and department. Example (plain text): Calle Lopez 42 Colonia El Carmen Ahuachapan Ahuachapan El Salvador

When you need more context
- Inspect `Ejemplo3.py` first for address/data-generation patterns. Use `Ejemplo2.py` and `Ejemplo1.py` for simpler examples of using `Faker` + PyQt5.

If you are an AI making changes
- Keep edits small and focused. Provide a short commit message explaining the intention (e.g., "refactor: extract email normalizer" or "feat: add new colonia to provider").
- If you add code that requires environment changes (new packages or different Qt bindings), include instructions in `README.md` and update `requirements.txt`.

Questions for the repo owner
- Should we split `Ejemplo3.py` into modules (provider + ui + runner)? If yes, prefer `faker_provider.py` and `ui.py` with simple imports so reviewers can run `python Ejemplo3.py` unchanged.

If anything here is unclear or you want a different level of detail (examples, tests, CI suggestions), tell me which area to expand.
