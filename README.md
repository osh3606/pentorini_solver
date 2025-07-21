# Pentorini Solver (펜토리니 솔버)

이 저장소는 고전 펜토미노 퍼즐의 변형인 펜토리니 퍼즐을 위한 솔버를 포함합니다. 펜토리니의 독특한 점은 퍼즐 구성이 현재 날짜와 요일에 따라 매일 바뀐다는 것입니다.

## 프로젝트 개요

이 프로젝트는 펜토리니 솔버의 명령줄 인터페이스(CLI) 버전과 그래픽 사용자 인터페이스(GUI) 버전을 모두 제공합니다.

-   **CLI 버전**: 텍스트 기반 퍼즐 해결 결과를 보여줍니다.
-   **GUI 버전**: 그래픽 기반 퍼즐 해결 괄과를 보여줍니다.(추천)

## 기능

*   현재 날짜와 요일을 기반 셀 선택에 따라 펜토리니 퍼즐의 해결책을 CLI, GUI 기반으로 제공합니다.

## 시작하기

### 전제 조건

Python 3.12.11 기반으로 프로그램이 작성되었습니다. 해당 버젼으로 실행 시키는 것이 가장 좋은 결과를 제공합니다. 다음 명령으로 Python 버전을 확인할 수 있습니다:

```bash
python --version
```

`pip`을 사용하여 필요한 종속성을 설치하십시오:

```bash
pip install -r requirement.txt
```

### Solver 실행

#### CLI 버전

CLI 솔버를 실행하려면 `solver.py`를 실행하십시오:

```bash
python solver.py
```

#### GUI 버전

GUI 애플리케이션을 시작하려면 `gui.py`를 실행하십시오:

```bash
python gui.py
```

## 프로젝트 구조

```
.
├── gui.py                # 그래픽 사용자 인터페이스 소스 코드
├── README.md             # 이 README 파일
├── requirement.txt       # Python 종속성
└── solver.py             # 핵심 퍼즐 해결 로직 (CLI 버전)
```

---

# Pentorini Solver

This repository contains a solver for Pentorini puzzles, a variation of the classic Pentomino puzzle. What makes Pentorini unique is that the puzzle configuration changes daily based on the current date and day of the week.

## Project Overview

This project provides both a Command Line Interface (CLI) version and a Graphical User Interface (GUI) version of the Pentorini solver.

-   **CLI Version**: Displays text-based puzzle solutions.
-   **GUI Version**: Displays graphic-based puzzle solutions (recommended).

## Features

*   Provides solutions for Pentorini puzzles based on the current date and day of the week, with cell selection, via both CLI and GUI.

## Getting Started

### Prerequisites

The program was developed based on Python 3.12.11. Running it with this version will provide the best results. You can check your Python version with the following command:

```bash
python --version
```

Install the necessary dependencies using `pip`:

```bash
pip install -r requirement.txt
```

### Running the Solver

#### CLI Version

To run the CLI solver, execute `solver.py`:

```bash
python solver.py
```

#### GUI Version

To start the GUI application, execute `gui.py`:

```bash
python gui.py
```

## Project Structure

```
.
├── gui.py                # Graphic User Interface source code
├── README.md             # This README file
├── requirement.txt       # Python dependencies
└── solver.py             # Core puzzle solving logic (CLI version)
```

---

# Pentorini Solver (ペントリニソルバー)

このリポジトリには、古典的なペントミノパズルの変形であるペントリニパズルのソルバーが含まれています。ペントリニのユニークな点は、パズルの構成が現在の日付と曜日に基づいて毎日変わることです。

## プロジェクト概要

このプロジェクトは、ペントリニソルバーのコマンドラインインターフェース（CLI）バージョンとグラフィカルユーザーインターフェース（GUI）バージョンの両方を提供します。

-   **CLIバージョン**: テキストベースのパズル解決結果を表示します。
-   **GUIバージョン**: グラフィックベースのパズル解決結果を表示します（推奨）。

## 機能

*   現在の日付と曜日に基づくセル選択に応じて、CLIおよびGUIベースでペントリニパズルの解決策を提供します。

## 始めるには

### 前提条件

プログラムはPython 3.12.11に基づいて作成されました。このバージョンで実行すると、最良の結果が得られます。次のコマンドでPythonのバージョンを確認できます。

```bash
python --version
```

`pip`を使用して必要な依存関係をインストールしてください。

```bash
pip install -r requirement.txt
```

### ソルバーの実行

#### CLIバージョン

CLIソルバーを実行するには、`solver.py`を実行します。

```bash
python solver.py
```

#### GUIバージョン

GUIアプリケーションを起動するには、`gui.py`を実行します。

```bash
python gui.py
```

## プロジェクト構造

```
.
├── gui.py                # グラフィカルユーザーインターフェースのソースコード
├── README.md             # このREADMEファイル
├── requirement.txt       # Pythonの依存関係
└── solver.py             # コアパズル解決ロジック（CLIバージョン）
```

*AI翻訳版*