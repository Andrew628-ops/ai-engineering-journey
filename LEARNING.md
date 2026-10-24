# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
I want to become a professional AI engineer. I'm currently learning Python and backend development.

What I most want to build by the end: a trained model.

Teach me from my current level, using simple English and real-life examples. Give me practical exercises and let me write the code myself.

Don't immediately give me answers when I make mistakes. Guide me with hints, test my understanding, and increase the difficulty gradually.

I also want to document my progress and projects on GitHub.

## Placement
- Date: 2026-10-22
- Score: 1/10 — Math & Statistics: 1/2; Classical ML: 0/2; Deep Learning: 0/2; NLP & Transformers: 0/2; Applied AI: 0/2
- Entry point: Phase 0: Setup & Tooling (learner-selected after placement)
- Pace: ~28 hours/week
- Evidence: Q1 answered A correctly; Q2–Q10 explicitly marked unknown. These are topics to learn, not demonstrated misconceptions. Python and backend proficiency were not assessed by this quiz.

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | 16 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 26 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP — Foundations to Advanced | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 76 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 34 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

Total estimated time for Review + Do: ~1,170 hours across 20 phases.
Source: [ROADMAP.md](https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/ROADMAP.md), retrieved 2026-10-22. Estimates use phase headings; the roadmap's headline total differs from their sum. Phase 19 includes the full capstone collection.

At 28 hours/week, the listed estimates total about 42 weeks. Exercises, revision, Python practice, and GitHub documentation can extend this; this is not a deadline or a promise of professional readiness.

Start with Phase 0, Lesson 01: Dev Environment, as explicitly requested by the learner. Complete Setup & Tooling before Math Foundations. Keep learner-written exercises, short reflections, project READMEs, and reproducible results ready for GitHub as learning progresses.

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-10-22 | 00-setup-and-tooling/01-dev-environment | 2/3 | Learner reported Linux, Python 3.12.3, Git 2.43.0, uv 0.13.5; created and activated .venv, ran Python/NumPy exercises and verify_setup.py, saved requirements.txt, ignored .venv, and drafted README setup. Corrected list repetition versus array multiplication. Review system foundation before package managers. NVIDIA access unconfirmed (nvidia-smi unavailable); PyTorch and official route preflight not yet run. Later runtimes deferred until needed. |

| 2026-10-23 | 00-setup-and-tooling/02-git-and-collaboration | 3/3 | Practised inspecting history, staging README changes, committing, pushing, creating practice/git-notes, merging into main, and ignoring model checkpoints; learner-reported status matched origin/main. Initially confused staging with commits and merge with push, then correctly completed the workflow and quiz. Warm-up correctly recalled package isolation and system foundation first. |

| 2026-10-23 | 00-setup-and-tooling/03-gpu-setup-and-cloud | 1/3 | Installed CPU PyTorch locally; ran device checks and CPU benchmark; used Colab T4 for synchronized GPU timing, measured about 24.81× speedup excluding transfers, and estimated FP16 weights-only capacity. Correctly answered synchronization question; review nvidia-smi and bytes-per-parameter arithmetic. Local artifacts and notes are in 03-gpu-setup-cloud/. |

| 2026-10-23 | 00-setup-and-tooling/03-gpu-setup-and-cloud | 2/3 (retry) | Retake: correctly recalled nvidia-smi and GPU synchronization; selected 24 billion instead of 12 billion for 24 GB of FP16 weights. Continue practising capacity = bytes / bytes per parameter. Original attempt retained above. |

| 2026-10-23 | 00-setup-and-tooling/04-apis-and-keys | 2/3 | Local simulation chosen by learner: loaded a fake key with environment variables and python-dotenv, tested missing-key handling, confirmed .env ignore rule, built a request dictionary and unsent HTTP POST, converted JSON in both directions, and extracted simulated responses using dictionary and object access. Outputs learner-reported; no live API call or provider SDK tested. Needed explanation of object attributes; review Anthropic x-api-key versus Content-Type. Local script: phases/00-setup-and-tooling/04-apis-keys/apis_setup.py. Warm-up correctly recalled FP16 capacity and GPU synchronization. |

| 2026-10-23 | 00-setup-and-tooling/04-apis-and-keys | 3/3 (retry) | Correctly recalled local key storage, Anthropic x-api-key authentication header, and HTTP 429 wait-before-retry behavior. Original attempt retained; quiz review item cleared. Live API and actual SDK practice remain deferred by learner choice. |

| 2026-10-23 | 00-setup-and-tooling/05-jupyter-notebooks | 3/3 | Practised in Google Colab: code and Markdown cells, shared kernel state, last-expression display, %%time and %timeit, random-number generation comparison (Python list 7.51 ms; NumPy array 0.971 ms), DataFrame display, bar chart, CSV save/load, and restart-and-run-all. Learner reported all cells completed after restart; notebook not inspected locally. Initially expected variables to survive a kernel restart, both expressions to auto-display, %timeit for a long training run, and the Python list to have the shorter timing bar; corrected through practice and quiz. GPU/Colab transfer exercise not performed this session. |

| 2026-10-24 | 00-setup-and-tooling/06-python-environments | 3/3 | Learner-reported verification of repository NumPy 2.5.4 versus practice environment 1.26.4; wrote pyproject.toml, generated uv.lock, and used uv sync --locked and uv run --locked to verify lesson .venv with NumPy 2.5.4. Corrected TOML field names, lockfile versus allowed requirements, active-shell versus uv project environment, and direct versus transitive dependencies. Correctly answered interpreter-path, pip/conda tracking, and CUDA-driver compatibility quiz questions. Ignore-rule output not supplied; official setup script, optional dependency groups, and torch/Anthropic installation exercises not performed. Global-install exercise avoided in favor of isolated practice. |

| 2026-10-24 | 00-setup-and-tooling/07-docker-for-ai | 1/3 | Conceptual walkthrough chosen because Docker engine socket access was denied and student lacks sudo/docker-group membership. Docker client 28.2.2 reported; no image build or container run completed, and Dockerfile creation not confirmed. Traced image/container distinction, FROM/WORKDIR/COPY/CMD, build context, unchanged image copies, writable layers versus persistent mounts, host:container ports, and Compose. Corrected mount persistence and host port predictions. Quiz: persistent mounts correct; review NVIDIA Container Toolkit exposing host GPUs (driver remains on host) and Compose service-name networking. Practical exercises remain pending authorized Docker access. |

| 2026-10-24 | 00-setup-and-tooling/07-docker-for-ai | 3/3 (retry) | Correctly recalled persistent mounts, NVIDIA Container Toolkit exposing host GPUs, and Compose service-name networking. Original attempt retained; quiz review cleared. Practical image-build and container-run exercises remain pending authorized Docker engine access. |

| 2026-10-24 | 00-setup-and-tooling/08-editor-setup | 2/3 | Learner reported VS Code Python, Pylance, Black, and Ruff installed; selected repository .venv interpreter, enabled basic type checking, observed and fixed string-to-int warning, configured Black as formatter and verified format-on-save, and observed Ruff F401 unused-import warning. Prefers Google Colab for notebooks; VS Code Jupyter extension deferred. Understood Remote SSH execution location; no remote connection tested. Review notebook.output.scrolling: contains long output in a scrollable area rather than enabling scrolling animations. |

| 2026-10-24 | 00-setup-and-tooling/08-editor-setup | 3/3 (retry) | Correctly recalled Remote SSH, notebook output scrolling, and basic type checking. Original attempt retained; lesson review item cleared. Colab remains the chosen notebook interface; remote connection not tested. |

| 2026-10-24 | 00-setup-and-tooling/09-data-management | 3/3 | Practised in Google Colab with 20 numbered examples: seeded shuffle, manual 14/3/3 slices, disjoint-ID reasoning, Hugging Face Dataset construction and seeded two-stage 70/15/15 split, repeated training-ID equality True, CSV/Parquet export (53 versus 949 bytes), Parquet reload (20 rows and matching IDs), and local CSV streaming of five rows. Needed stepwise help with percentage counts and slice end indices. Correctly answered Parquet, streaming, and DVC quiz questions. Outputs learner-reported; notebook not inspected locally. Remote Hub dataset/model downloads, remote streaming, and actual LFS/DVC setup not performed. |

## Review queue
- 00-setup-and-tooling/07-docker-for-ai — Practical follow-up: image builds and container runs remain untested pending authorized Docker engine access. Latest quiz 3/3; conceptual walkthrough and quiz retake completed.
- 00-setup-and-tooling/03-gpu-setup-and-cloud — Latest quiz 2/3 (67%), improved from 1/3: NVIDIA status check now recalled correctly; continue reviewing FP16 weights-only arithmetic (24 billion bytes / 2 bytes per parameter = 12 billion parameters). Training requires extra memory. Notes: phases/00-setup-and-tooling/03-gpu-setup-cloud/NOTES.md.
- 00-setup-and-tooling/01-dev-environment — Quiz 2/3 (67%): review environment setup order, especially why the operating system and shell must be ready before package managers. Follow up on PyTorch and official beginner preflight before model-training exercises; verify_setup.py currently checks only Python, NumPy, and virtual-environment activation.
