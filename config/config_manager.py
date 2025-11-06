"""
Configuration Manager for Professional GUI Application
Handles application settings, window state, and user preferences
"""

import json
import os
from pathlib import Path


class ConfigManager:
    def __init__(self):
        self.config_dir = Path.home() / ".professional_gui_app"
        self.config_file = self.config_dir / "config.json"
        self.default_config = {
            "theme": "light",
            "window": {
                "width": 1920,
                "height": 1080,
                "x": 100,
                "y": 100,
                "maximized": False
            },
            "sidebar": {
                "collapsed": False,
                "width": 250
            },
            "tabs": {
                "current_main_tab": 0,
                "current_sub_tabs": [0, 0, 0, 0, 0]  # Sub-tab index for each main tab
            },
            "ui": {
                "font_size": 14,
                "auto_collapse_sidebar": True,
                "auto_collapse_threshold": 1200
            }
        }
        self.config = self.load_config()
    
    def ensure_config_dir(self):
        """Ensure the configuration directory exists"""
        self.config_dir.mkdir(exist_ok=True)
    
    def load_config(self):
        """Load configuration from file or create default"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                    # Merge with defaults to handle new settings
                    return self.merge_configs(self.default_config, loaded_config)
            else:
                return self.default_config.copy()
        except Exception as e:
            print(f"Error loading config: {e}")
            return self.default_config.copy()
    
    def save_config(self):
        """Save current configuration to file"""
        try:
            self.ensure_config_dir()
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def merge_configs(self, default, loaded):
        """Recursively merge configurations, preferring loaded values"""
        result = default.copy()
        for key, value in loaded.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self.merge_configs(result[key], value)
            else:
                result[key] = value
        return result
    
    def get(self, key, default=None):
        """Get a configuration value using dot notation (e.g., 'window.width')"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key, value):
        """Set a configuration value using dot notation"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
    
    def get_theme(self):
        """Get current theme"""
        return self.config.get("theme", "light")
    
    def set_theme(self, theme):
        """Set current theme"""
        self.config["theme"] = theme
        self.save_config()
    
    def get_window_config(self):
        """Get window configuration"""
        return self.config.get("window", self.default_config["window"])
    
    def set_window_config(self, width, height, x, y, maximized=False):
        """Set window configuration"""
        self.config["window"] = {
            "width": width,
            "height": height,
            "x": x,
            "y": y,
            "maximized": maximized
        }
        self.save_config()
    
    def get_sidebar_config(self):
        """Get sidebar configuration"""
        return self.config.get("sidebar", self.default_config["sidebar"])
    
    def set_sidebar_config(self, collapsed, width=250):
        """Set sidebar configuration"""
        self.config["sidebar"] = {
            "collapsed": collapsed,
            "width": width
        }
        self.save_config()
    
    def get_tab_config(self):
        """Get tab configuration"""
        return self.config.get("tabs", self.default_config["tabs"])
    
    def set_current_main_tab(self, index):
        """Set current main tab index"""
        if "tabs" not in self.config:
            self.config["tabs"] = self.default_config["tabs"].copy()
        self.config["tabs"]["current_main_tab"] = index
        self.save_config()
    
    def set_current_sub_tab(self, main_tab_index, sub_tab_index):
        """Set current sub-tab index for a main tab"""
        if "tabs" not in self.config:
            self.config["tabs"] = self.default_config["tabs"].copy()
        if "current_sub_tabs" not in self.config["tabs"]:
            self.config["tabs"]["current_sub_tabs"] = [0, 0, 0, 0, 0]
        
        while len(self.config["tabs"]["current_sub_tabs"]) <= main_tab_index:
            self.config["tabs"]["current_sub_tabs"].append(0)
            
        self.config["tabs"]["current_sub_tabs"][main_tab_index] = sub_tab_index
        self.save_config()
    
    def get_ui_config(self):
        """Get UI configuration"""
        return self.config.get("ui", self.default_config["ui"])
    
    def reset_to_defaults(self):
        """Reset configuration to defaults"""
        self.config = self.default_config.copy()
        self.save_config()
    
    def export_config(self, file_path):
        """Export configuration to a file"""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            print(f"Error exporting config: {e}")
            return False
    
    def import_config(self, file_path):
        """Import configuration from a file"""
        try:
            with open(file_path, 'r') as f:
                imported_config = json.load(f)
                self.config = self.merge_configs(self.default_config, imported_config)
                self.save_config()
            return True
        except Exception as e:
            print(f"Error importing config: {e}")
            return False
