"""
Theme Manager for Professional GUI Application
Provides Light, Dark, and Colorful themes with responsive design
"""

class ThemeManager:
    def __init__(self):
        self.current_theme = "light"
        
    def get_light_theme(self):
        return """
        QMainWindow {
            background-color: #ffffff;
            color: #333333;
        }
        
        #themeButton {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-size: 14px;
        }
        
        #themeButton:hover {
            background-color: #0056b3;
        }
        
        /* Sidebar Styling */
        #sidebar {
            background-color: #f8f9fa;
            border-right: 1px solid #dee2e6;
            min-width: 250px;
            max-width: 250px;
        }
        
        #sidebar QPushButton {
            background-color: transparent;
            border: none;
            padding: 12px 16px;
            text-align: left;
            color: #495057;
            font-size: 14px;
            border-radius: 4px;
            margin: 2px;
        }
        
        #sidebar QPushButton:hover {
            background-color: #e9ecef;
            color: #212529;
        }
        
        #sidebar QPushButton:checked {
            background-color: #007bff;
            color: white;
        }
        
        #collapseButton {
            background-color: #6c757d;
            color: white;
            border: none;
            padding: 8px;
            margin: 5px;
            border-radius: 4px;
        }
        
        #collapseButton:hover {
            background-color: #5a6268;
        }
        
        /* Collapsed sidebar styling */
        #sidebar[collapsed="true"] {
            min-width: 50px;
            max-width: 50px;
        }
        
        #sidebar[collapsed="true"] QPushButton {
            text-align: center;
            padding: 12px 4px;
            font-size: 16px;
        }
        
        /* Main Content Area */
        #mainContent {
            background-color: #ffffff;
            padding: 20px;
        }
        
        /* Tab Widget Styling */
        QTabWidget::pane {
            border: 1px solid #dee2e6;
            background-color: #ffffff;
            border-radius: 4px;
        }
        
        QTabBar::tab {
            background-color: #f8f9fa;
            color: #495057;
            padding: 10px 16px;
            margin-right: 2px;
            border: 1px solid #dee2e6;
            border-bottom: none;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }
        
        QTabBar::tab:selected {
            background-color: #ffffff;
            color: #212529;
            border-bottom: 1px solid #ffffff;
        }
        
        QTabBar::tab:hover {
            background-color: #e9ecef;
        }
        
        /* Content Area Labels */
        QLabel {
            color: #495057;
            font-size: 14px;
        }
        
        /* Scrollbar Styling */
        QScrollBar:vertical {
            background-color: #f8f9fa;
            width: 12px;
            border-radius: 6px;
        }
        
        QScrollBar::handle:vertical {
            background-color: #dee2e6;
            border-radius: 6px;
            min-height: 20px;
        }
        
        QScrollBar::handle:vertical:hover {
            background-color: #adb5bd;
        }
        """
    
    def get_dark_theme(self):
        return """
        QMainWindow {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        
        #themeButton {
            background-color: #0d7377;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-size: 14px;
        }
        
        #themeButton:hover {
            background-color: #14a085;
        }
        
        /* Sidebar Styling */
        #sidebar {
            background-color: #2d2d2d;
            border-right: 1px solid #404040;
            min-width: 250px;
            max-width: 250px;
        }
        
        #sidebar QPushButton {
            background-color: transparent;
            border: none;
            padding: 12px 16px;
            text-align: left;
            color: #cccccc;
            font-size: 14px;
            border-radius: 4px;
            margin: 2px;
        }
        
        #sidebar QPushButton:hover {
            background-color: #404040;
            color: #ffffff;
        }
        
        #sidebar QPushButton:checked {
            background-color: #0d7377;
            color: white;
        }
        
        #collapseButton {
            background-color: #404040;
            color: white;
            border: none;
            padding: 8px;
            margin: 5px;
            border-radius: 4px;
        }
        
        #collapseButton:hover {
            background-color: #525252;
        }
        
        /* Main Content Area */
        #mainContent {
            background-color: #1a1a1a;
            padding: 20px;
        }
        
        /* Tab Widget Styling */
        QTabWidget::pane {
            border: 1px solid #404040;
            background-color: #1a1a1a;
            border-radius: 4px;
        }
        
        QTabBar::tab {
            background-color: #2d2d2d;
            color: #cccccc;
            padding: 10px 16px;
            margin-right: 2px;
            border: 1px solid #404040;
            border-bottom: none;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }
        
        QTabBar::tab:selected {
            background-color: #1a1a1a;
            color: #ffffff;
            border-bottom: 1px solid #1a1a1a;
        }
        
        QTabBar::tab:hover {
            background-color: #404040;
        }
        
        /* Content Area Labels */
        QLabel {
            color: #cccccc;
            font-size: 14px;
        }
        
        /* Scrollbar Styling */
        QScrollBar:vertical {
            background-color: #2d2d2d;
            width: 12px;
            border-radius: 6px;
        }
        
        QScrollBar::handle:vertical {
            background-color: #404040;
            border-radius: 6px;
            min-height: 20px;
        }
        
        QScrollBar::handle:vertical:hover {
            background-color: #525252;
        }
        """
    
    def get_colorful_theme(self):
        return """
        QMainWindow {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 #667eea, stop:1 #764ba2);
            color: #ffffff;
        }
        
        #themeButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #a8e6cf, stop:1 #88d8c0);
            color: #2c3e50;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: bold;
        }
        
        #themeButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #74b9ff, stop:1 #0984e3);
            color: white;
        }
        
        /* Sidebar Styling */
        #sidebar {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                stop:0 #a8e6cf, stop:1 #74b9ff);
            border-right: 3px solid #fd79a8;
            min-width: 250px;
            max-width: 250px;
        }
        
        #sidebar QPushButton {
            background-color: rgba(255, 255, 255, 0.1);
            border: 2px solid transparent;
            padding: 12px 16px;
            text-align: left;
            color: #2c3e50;
            font-size: 14px;
            font-weight: bold;
            border-radius: 15px;
            margin: 3px;
        }
        
        #sidebar QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #fd79a8, stop:1 #fdcb6e);
            color: white;
            border: 2px solid #ffffff;
        }
        
        #sidebar QPushButton:checked {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #6c5ce7, stop:1 #fd79a8);
            color: white;
            border: 2px solid #ffffff;
        }
        
        #collapseButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #fd79a8, stop:1 #fdcb6e);
            color: white;
            border: 2px solid #ffffff;
            padding: 8px;
            margin: 5px;
            border-radius: 15px;
            font-weight: bold;
        }
        
        #collapseButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #00b894, stop:1 #55a3ff);
        }
        
        /* Main Content Area */
        #mainContent {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 rgba(255, 255, 255, 0.9), stop:1 rgba(240, 248, 255, 0.9));
            padding: 20px;
            border-radius: 15px;
            margin: 10px;
        }
        
        /* Tab Widget Styling */
        QTabWidget::pane {
            border: 3px solid #fd79a8;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 rgba(255, 255, 255, 0.95), stop:1 rgba(168, 230, 207, 0.3));
            border-radius: 15px;
        }
        
        QTabBar::tab {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #74b9ff, stop:1 #0984e3);
            color: white;
            padding: 12px 20px;
            margin-right: 3px;
            border: 2px solid #fd79a8;
            border-bottom: none;
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
            font-weight: bold;
        }
        
        QTabBar::tab:selected {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #fd79a8, stop:1 #fdcb6e);
            color: white;
            border-bottom: 3px solid #fd79a8;
        }
        
        QTabBar::tab:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #a29bfe, stop:1 #fd79a8);
        }
        
        /* Content Area Labels */
        QLabel {
            color: #2c3e50;
            font-size: 14px;
            font-weight: bold;
        }
        
        /* Scrollbar Styling */
        QScrollBar:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #a8e6cf, stop:1 #74b9ff);
            width: 15px;
            border-radius: 7px;
        }
        
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #fd79a8, stop:1 #fdcb6e);
            border-radius: 7px;
            min-height: 25px;
            border: 2px solid #ffffff;
        }
        
        QScrollBar::handle:vertical:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                stop:0 #6c5ce7, stop:1 #fd79a8);
        }
        """
    
    def get_theme_style(self, theme_name):
        """Get the stylesheet for the specified theme"""
        if theme_name == "light":
            return self.get_light_theme()
        elif theme_name == "dark":
            return self.get_dark_theme()
        elif theme_name == "colorful":
            return self.get_colorful_theme()
        else:
            return self.get_light_theme()
    
    def set_theme(self, theme_name):
        """Set the current theme"""
        self.current_theme = theme_name
    
    def get_current_theme(self):
        """Get the current theme name"""
        return self.current_theme
