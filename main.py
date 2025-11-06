"""
Professional GUI Application
A responsive Python application built with PySide6 featuring:
- 3 themes (Light, Dark, Colorful)
- Responsive design for all screen sizes
- Collapsible sidebar
- Professional layout with header, sidebar, content area, and footer
- 5 main navigation tabs with 4 sub-tabs each
"""

import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

# Add gui module to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'gui'))

from gui.main_window import ResponsiveMainWindow


def main():
    """Main application entry point"""
    # Enable high DPI scaling for better display on different screen densities
    # Note: These attributes are deprecated in newer Qt versions but still functional
    try:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    except AttributeError:
        # These attributes might not be available in newer Qt versions
        pass
    
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Professional GUI Application")
    app.setApplicationDisplayName("Professional GUI Application")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Your Organization")
    app.setOrganizationDomain("yourorganization.com")
    
    # Create and show the main window
    try:
        window = ResponsiveMainWindow()
        window.show()
        
        # Center the window on screen
        screen = app.primaryScreen().geometry()
        window_geometry = window.geometry()
        x = (screen.width() - window_geometry.width()) // 2
        y = (screen.height() - window_geometry.height()) // 2
        window.move(x, y)
        
        print("Application started successfully!")
        print(f"Window size: {window.width()}x{window.height()}")
        print(f"Theme: {window.theme_manager.get_current_theme()}")
        
        return app.exec()
        
    except Exception as e:
        print(f"Error starting application: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
