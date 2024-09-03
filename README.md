# rl_ad_mini_project

## Installation and Usage

```
git clone https://github.com/brnmj/rl_ad_mini_project.git
```

```
python -m venv .venv --upgrade-deps --copies --upgrade --prompt="rl_ad"
```

```
.\.venv\Scripts\pip install requirements.txt
```

```
cd scripts
```

```
..\.venv\Scripts\python.exe experiments.py evaluate .\configs\HighwayEnv\env.json .\configs\HighwayEnv\agents\DQNAgent\dqn.json --recover --train --episodes=200 --no-display --verbose
```

```
..\.venv\Scripts\python.exe experiments.py evaluate .\configs\HighwayEnv\env.json .\configs\HighwayEnv\agents\DQNAgent\dqn.json --recover --test --episodes=5 --verbose
```

```
..\.venv\Scripts\python.exe experiments.py evaluate .\configs\IntersectionEnv\env.json .\configs\IntersectionEnv\agents\DQNAgent\ego_attention.json --recover --train --episodes=200 --no-display --verbose
```

```
..\.venv\Scripts\python.exe experiments.py evaluate .\configs\IntersectionEnv\env.json .\configs\IntersectionEnv\agents\DQNAgent\ego_attention.json --recover --test --episodes=5 --verbose
```