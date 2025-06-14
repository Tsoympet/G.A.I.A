# GAIA Module Reference

This document provides a high-level overview of each module within the GAIA architecture.

---

## Core Modules

### `gaia.core.intelligence_engine`
- Manages the knowledge base, inference logic, and reasoning tools.

### `gaia.core.emotion_engine`
- Tracks mood, emotional state, and influences behavior/dreams.

### `gaia.core.dream_state_engine`
- Generates nightly dream sequences, memory-triggered reflections, and mood evolution.

### `gaia.core.self_repair`
- Includes diagnostics and self-healing mechanisms for modules.

### `gaia.core.plugin_registry`
- Handles dynamic plugin event triggering and registration.

---

## Modules

### `gaia.modules.crypto`
- Live crypto market analysis, wallet tracking, and DeFi intelligence.

### `gaia.modules.stock`
- Stock screener, regional portfolios, and earnings predictions.

### `gaia.modules.betting`
- Sports betting predictions, bankroll tracking, and API integrations.

### `gaia.modules.casino`
- Includes:
  - `crash_logic.py`: Crash game multiplier prediction
  - `baccarat_logic.py`: Streak tracking for baccarat
  - `poker_logic.py`: Bluff detection and stats logging

### `gaia.modules.voice`
- ATHENA voice system, text-to-speech and speech recognition.

---

## GUI

### `gaia.gui.dashboard`
- Central panel for navigation, module access, and voice interaction.

### `gaia.gui.settings_panel`
- Personalization, user configs, and ethical switches.

### `gaia.gui.modules.casino_games_gui`
- Casino-specific game interface elements.

### `gaia.gui.stl_viewer`
- Viewer for 3D G-code paths and models.

---

## Advanced Systems

### `gaia.plugins.quantum_forecaster`
- Experimental long-term prediction engine using hybrid neural models.

### `gaia.plugins.multi_agent_trainer`
- Reinforcement training for multiplayer or multi-agent games.

### `gaia.plugins.emotion_feedback_loop`
- Adjusts prediction behavior based on real-time emotional analysis.

---

## Portal + Mobile

### `portal/`
- License key activation, validation, and user dashboard.

### `mobile/`
- Sync layer for GAIA mobile app and Firebase integration.

---

## Data & Exports

### `data/emotional_memory.json`
- Stores evolving mood patterns and triggers.

### `data/knowledge_base.db`
- Embedded vector DB + seed knowledge.

### `scripts/export_manager.py`
- Manages PDF, CSV, JSON exports of reports, sessions, and dreams.

---

This documentation will evolve with new plugin integrations and AI modules.
