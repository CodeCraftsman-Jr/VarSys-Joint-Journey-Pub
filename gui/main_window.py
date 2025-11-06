"""
Main Window Component for Professional GUI Application
Features responsive design with collapsible sidebar and tabbed interface
"""

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                              QPushButton, QLabel, QTabWidget, QSplitter, 
                              QScrollArea, QFrame, QApplication, QSizePolicy)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize, QTimer
from PySide6.QtGui import QFont, QIcon
import sys
import os

# Add the project root to the path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from themes.theme_manager import ThemeManager
from config.config_manager import ConfigManager
from gui.demo_content import DashboardDemo, AnalyticsDemo, SettingsDemo, UsersDemo, ReportsDemo


class ResponsiveMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme_manager = ThemeManager()
        self.config_manager = ConfigManager()
        self.sidebar_collapsed = False
        self.current_tab_index = 0
        
        # Load saved configuration
        self.load_saved_state()
        
        # Set minimum window size for responsive design
        self.setMinimumSize(1366, 768)  # Minimum laptop screen size
        
        self.init_ui()
        self.apply_theme()
        
        # Setup responsive behavior
        self.setup_responsive_behavior()
        
        # Restore window state
        self.restore_window_state()
        
        # Apply saved sidebar state after UI is ready
        self.apply_saved_sidebar_state()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Professional GUI Application")
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create main content area with sidebar (no header/footer)
        self.create_main_content(main_layout)
        
    def create_main_content(self, parent_layout):
        """Create the main content area with sidebar and content"""
        # Create splitter for responsive layout
        self.main_splitter = QSplitter(Qt.Horizontal)
        self.main_splitter.setChildrenCollapsible(False)  # Prevent complete collapse
        
        # Create sidebar
        self.create_sidebar()
        
        # Set initial expanded state
        self.sidebar_container.setMinimumWidth(250)
        self.sidebar_container.setMaximumWidth(250)
        self.sidebar_container.setFixedWidth(250)
        
        # Create main content area
        self.create_content_area()
        
        # Add widgets to splitter
        self.main_splitter.addWidget(self.sidebar_container)
        self.main_splitter.addWidget(self.content_container)
        
        # Set initial sizes (sidebar: 250px, content: rest)
        self.main_splitter.setSizes([250, 1000])
        
        parent_layout.addWidget(self.main_splitter)
        
    def create_sidebar(self):
        """Create the collapsible sidebar"""
        self.sidebar_container = QFrame()
        self.sidebar_container.setObjectName("sidebar")
        # Don't set fixed constraints initially - let toggle handle it
        
        sidebar_layout = QVBoxLayout(self.sidebar_container)
        
        # Collapse button
        self.collapse_button = QPushButton("☰ Collapse")
        self.collapse_button.setObjectName("collapseButton")
        self.collapse_button.clicked.connect(self.toggle_sidebar)
        sidebar_layout.addWidget(self.collapse_button)
        
        # Theme switcher button
        self.theme_button = QPushButton("🎨 Theme")
        self.theme_button.setObjectName("themeButton")
        self.theme_button.clicked.connect(self.cycle_theme)
        sidebar_layout.addWidget(self.theme_button)
        
        # Create 5 main navigation buttons
        self.nav_buttons = []
        self.nav_items = [
            ("📊", "Dashboard"),
            ("📈", "Analytics"), 
            ("⚙️", "Settings"),
            ("👥", "Users"),
            ("📋", "Reports")
        ]
        
        for i, (icon, text) in enumerate(self.nav_items):
            button = QPushButton(f"{icon} {text}")
            button.setCheckable(True)
            button.clicked.connect(lambda checked, idx=i: self.switch_main_tab(idx))
            if i == 0:  # Select first tab by default
                button.setChecked(True)
            self.nav_buttons.append(button)
            sidebar_layout.addWidget(button)
            
        sidebar_layout.addStretch()
        
    def create_content_area(self):
        """Create the main content area with tabs"""
        self.content_container = QFrame()
        self.content_container.setObjectName("mainContent")
        
        content_layout = QVBoxLayout(self.content_container)
        
        # Create tab widget for main content
        self.main_tab_widget = QTabWidget()
        
        # Create 5 main tabs, each with 4 sub-tabs
        main_tabs = ["Dashboard", "Analytics", "Settings", "Users", "Reports"]
        
        for main_tab_idx, main_tab_name in enumerate(main_tabs):
            # Create sub-tab widget for each main tab
            sub_tab_widget = QTabWidget()
            
            # Create 4 sub-tabs for each main tab
            for i in range(4):
                sub_tab_content = self.create_tab_content(f"{main_tab_name} - Sub Tab {i+1}")
                sub_tab_widget.addTab(sub_tab_content, f"Sub Tab {i+1}")
            
            # Restore saved sub-tab state
            tab_config = self.config_manager.get_tab_config()
            saved_sub_tabs = tab_config.get("current_sub_tabs", [0, 0, 0, 0, 0])
            if main_tab_idx < len(saved_sub_tabs):
                sub_tab_widget.setCurrentIndex(saved_sub_tabs[main_tab_idx])
            
            self.main_tab_widget.addTab(sub_tab_widget, main_tab_name)
        
        # Set current main tab from saved state
        self.main_tab_widget.setCurrentIndex(self.current_tab_index)
        
        content_layout.addWidget(self.main_tab_widget)
        
    def create_tab_content(self, title):
        """Create content for a tab with placeholder text or demo content"""
        # Check if this is a main demo tab
        demo_widgets = {
            "Dashboard - Sub Tab 1": DashboardDemo(),
            "Analytics - Sub Tab 1": AnalyticsDemo(),
            "Settings - Sub Tab 1": SettingsDemo(),
            "Users - Sub Tab 1": UsersDemo(),
            "Reports - Sub Tab 1": ReportsDemo(),
        }
        
        if title in demo_widgets:
            return demo_widgets[title]
        
        # Default placeholder content for other tabs
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        
        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Placeholder content
        placeholder_text = f"""
        <h3>Welcome to {title}</h3>
        <p>This is a placeholder content area for the <strong>{title}</strong> section.</p>
        <p>Here you can add your application-specific content such as:</p>
        <ul>
            <li>Data visualization components</li>
            <li>Forms and input controls</li>
            <li>Tables and lists</li>
            <li>Charts and graphs</li>
            <li>Custom widgets and controls</li>
        </ul>
        <p>The layout is fully responsive and will adapt to different screen sizes.</p>
        <p>You can customize the styling through the theme manager to match your application's branding.</p>
        <p><strong>Pro tip:</strong> Check out the first sub-tab in each main section for interactive demo content!</p>
        """
        
        content_label = QLabel(placeholder_text)
        content_label.setWordWrap(True)
        content_label.setAlignment(Qt.AlignTop)
        
        # Make content scrollable
        scroll_area = QScrollArea()
        scroll_area.setWidget(content_label)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)
        
        return content_widget
        
    def toggle_sidebar(self):
        """Toggle sidebar collapsed/expanded state"""
        if not self.sidebar_collapsed:
            # Collapse sidebar - change to icon mode
            self.sidebar_container.setMinimumWidth(50)
            self.sidebar_container.setMaximumWidth(50)
            self.sidebar_container.setFixedWidth(50)
            
            # Update collapse button
            self.collapse_button.setText("☰")
            
            # Update theme button
            self.theme_button.setText("🎨")
            self.theme_button.setToolTip("Switch Theme")
            
            # Update navigation buttons to show only icons
            for i, button in enumerate(self.nav_buttons):
                icon, text = self.nav_items[i]
                button.setText(icon)
                button.setToolTip(text)
                
            self.sidebar_collapsed = True
            
        else:
            # Expand sidebar - change to full text mode
            self.sidebar_container.setMinimumWidth(250)
            self.sidebar_container.setMaximumWidth(250)
            self.sidebar_container.setFixedWidth(250)
            
            # Update collapse button
            self.collapse_button.setText("☰ Collapse")
            
            # Update theme button
            self.theme_button.setText("🎨 Theme")
            self.theme_button.setToolTip("")
            
            # Update navigation buttons to show full text
            for i, button in enumerate(self.nav_buttons):
                icon, text = self.nav_items[i]
                button.setText(f"{icon} {text}")
                button.setToolTip("")
                
            self.sidebar_collapsed = False
            
        # Force layout updates
        self.sidebar_container.updateGeometry()
        self.main_splitter.update()
        
        # Use a timer to force the splitter to respect the new sizes
        QTimer.singleShot(10, lambda: self.main_splitter.setSizes([
            50 if self.sidebar_collapsed else 250,
            self.width() - (50 if self.sidebar_collapsed else 250)
        ]))
        
        self.update()
            
    def switch_main_tab(self, index):
        """Switch to the specified main tab"""
        # Update button states
        for i, button in enumerate(self.nav_buttons):
            button.setChecked(i == index)
            
        # Switch tab content
        self.main_tab_widget.setCurrentIndex(index)
        self.current_tab_index = index
        
    def cycle_theme(self):
        """Cycle through available themes"""
        themes = ["light", "dark", "colorful"]
        current_index = themes.index(self.theme_manager.get_current_theme())
        next_index = (current_index + 1) % len(themes)
        new_theme = themes[next_index]
        
        self.theme_manager.set_theme(new_theme)
        self.apply_theme()
        
    def apply_theme(self):
        """Apply the current theme to the application"""
        stylesheet = self.theme_manager.get_theme_style(self.theme_manager.get_current_theme())
        self.setStyleSheet(stylesheet)
            
    def setup_responsive_behavior(self):
        """Setup responsive behavior for different screen sizes"""
        # Connect to resize events for responsive adjustments
        self.resizeEvent = self.on_window_resize
        
        # Initial responsive setup
        self.adjust_for_screen_size()
        
    def on_window_resize(self, event):
        """Handle window resize events for responsive design"""
        super().resizeEvent(event)
        self.adjust_for_screen_size()
        
    def adjust_for_screen_size(self):
        """Adjust UI elements based on current window size"""
        width = self.width()
        height = self.height()
        
        # Auto-collapse sidebar for very small screens
        if width < 1200 and not self.sidebar_collapsed:
            self.toggle_sidebar()
        elif width >= 1400 and self.sidebar_collapsed:
            self.toggle_sidebar()
            
        # Adjust font sizes for different screen sizes
        if width < 1366:
            # Small screen adjustments
            base_font_size = 12
        elif width < 1920:
            # Medium screen adjustments  
            base_font_size = 14
        else:
            # Large screen adjustments
            base_font_size = 16
            
        # Update fonts dynamically (this would be expanded for full responsive design)
        
    def closeEvent(self, event):
        """Handle application close event"""
        # Save current state before closing
        self.save_current_state()
        event.accept()
    
    def load_saved_state(self):
        """Load saved application state"""
        # Load theme
        saved_theme = self.config_manager.get_theme()
        self.theme_manager.set_theme(saved_theme)
        
        # Load sidebar state - temporarily force to False for testing
        sidebar_config = self.config_manager.get_sidebar_config()
        self.sidebar_collapsed = False  # Force expanded state initially
        
        # Load tab state
        tab_config = self.config_manager.get_tab_config()
        self.current_tab_index = tab_config.get("current_main_tab", 0)
    
    def restore_window_state(self):
        """Restore window size and position"""
        window_config = self.config_manager.get_window_config()
        
        if window_config.get("maximized", False):
            self.showMaximized()
        else:
            self.resize(window_config.get("width", 1920), window_config.get("height", 1080))
            self.move(window_config.get("x", 100), window_config.get("y", 100))
    
    def apply_saved_sidebar_state(self):
        """Apply the saved sidebar collapsed state"""
        if self.sidebar_collapsed:
            # If sidebar should be collapsed, apply the collapsed state
            self.sidebar_container.setMaximumWidth(50)
            self.sidebar_container.setMinimumWidth(50)
            self.sidebar_container.setFixedWidth(50)
            self.collapse_button.setText("☰")
            
            # Update theme button for collapsed state
            self.theme_button.setText("🎨")
            self.theme_button.setToolTip("Switch Theme")
            
            # Show only icons in navigation buttons
            for i, button in enumerate(self.nav_buttons):
                icon, _ = self.nav_items[i]
                button.setText(icon)
                button.setToolTip(self.nav_items[i][1])  # Show full name as tooltip
                
            # Force layout update
            self.main_splitter.setSizes([50, self.width() - 50])
        else:
            # Ensure expanded state is properly set
            self.sidebar_container.setMinimumWidth(250)
            self.sidebar_container.setMaximumWidth(250)
            self.sidebar_container.setFixedWidth(250)
            
            # Force layout update
            self.main_splitter.setSizes([250, self.width() - 250])
            
        # Force updates
        self.sidebar_container.updateGeometry()
        self.main_splitter.update()
    
    def save_current_state(self):
        """Save current application state"""
        # Save theme
        self.config_manager.set_theme(self.theme_manager.get_current_theme())
        
        # Save window state
        if not self.isMaximized():
            self.config_manager.set_window_config(
                self.width(), self.height(), 
                self.x(), self.y(), 
                self.isMaximized()
            )
        else:
            self.config_manager.set_window_config(
                1920, 1080, 100, 100, True
            )
        
        # Save sidebar state
        self.config_manager.set_sidebar_config(self.sidebar_collapsed)
        
        # Save current tab
        self.config_manager.set_current_main_tab(self.current_tab_index)
        
        # Save sub-tab states
        for i in range(self.main_tab_widget.count()):
            sub_tab_widget = self.main_tab_widget.widget(i)
            if isinstance(sub_tab_widget, QTabWidget):
                self.config_manager.set_current_sub_tab(i, sub_tab_widget.currentIndex())


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Professional GUI Application")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Your Organization")
    
    # Create and show main window
    window = ResponsiveMainWindow()
    window.show()
    
    # Center window on screen
    screen = app.primaryScreen().geometry()
    window_geometry = window.geometry()
    x = (screen.width() - window_geometry.width()) // 2
    y = (screen.height() - window_geometry.height()) // 2
    window.move(x, y)
    
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
