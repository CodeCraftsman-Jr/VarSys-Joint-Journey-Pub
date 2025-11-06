"""
Demo Content Widgets for Professional GUI Application
Provides sample content to demonstrate the application's capabilities
"""

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                              QPushButton, QProgressBar, QTableWidget, 
                              QTableWidgetItem, QTextEdit, QGridLayout,
                              QFrame, QSlider, QSpinBox, QComboBox,
                              QCheckBox, QRadioButton, QGroupBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
import random


class DashboardDemo(QWidget):
    """Dashboard demo with charts and statistics"""
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Dashboard Overview")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Statistics grid
        stats_layout = QGridLayout()
        
        stats = [
            ("Active Users", "1,234", "#28a745"),
            ("Revenue", "$45,678", "#007bff"),
            ("Orders", "89", "#ffc107"),
            ("Performance", "95%", "#17a2b8")
        ]
        
        for i, (label, value, color) in enumerate(stats):
            stat_widget = self.create_stat_widget(label, value, color)
            stats_layout.addWidget(stat_widget, i // 2, i % 2)
            
        layout.addLayout(stats_layout)
        
        # Progress indicators
        progress_group = QGroupBox("Progress Indicators")
        progress_layout = QVBoxLayout(progress_group)
        
        for label in ["Server Load", "Memory Usage", "Disk Space"]:
            progress_bar = QProgressBar()
            progress_bar.setValue(random.randint(30, 95))
            progress_layout.addWidget(QLabel(label))
            progress_layout.addWidget(progress_bar)
            
        layout.addWidget(progress_group)
        
    def create_stat_widget(self, label, value, color):
        widget = QFrame()
        widget.setFrameStyle(QFrame.StyledPanel)
        layout = QVBoxLayout(widget)
        
        value_label = QLabel(value)
        value_label.setFont(QFont("Arial", 20, QFont.Bold))
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setStyleSheet(f"color: {color};")
        
        desc_label = QLabel(label)
        desc_label.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(value_label)
        layout.addWidget(desc_label)
        
        return widget


class AnalyticsDemo(QWidget):
    """Analytics demo with data table and controls"""
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Analytics Data")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Controls
        controls_layout = QHBoxLayout()
        
        date_combo = QComboBox()
        date_combo.addItems(["Last 7 days", "Last 30 days", "Last 90 days", "Last year"])
        controls_layout.addWidget(QLabel("Time Period:"))
        controls_layout.addWidget(date_combo)
        
        refresh_btn = QPushButton("Refresh Data")
        refresh_btn.clicked.connect(self.refresh_data)
        controls_layout.addWidget(refresh_btn)
        controls_layout.addStretch()
        
        layout.addLayout(controls_layout)
        
        # Data table
        self.table = QTableWidget(10, 4)
        self.table.setHorizontalHeaderLabels(["Date", "Views", "Clicks", "Revenue"])
        self.refresh_data()
        layout.addWidget(self.table)
        
    def refresh_data(self):
        """Refresh table with random demo data"""
        for row in range(10):
            self.table.setItem(row, 0, QTableWidgetItem(f"2025-08-{row+1:02d}"))
            self.table.setItem(row, 1, QTableWidgetItem(str(random.randint(100, 1000))))
            self.table.setItem(row, 2, QTableWidgetItem(str(random.randint(10, 100))))
            self.table.setItem(row, 3, QTableWidgetItem(f"${random.randint(100, 500)}"))


class SettingsDemo(QWidget):
    """Settings demo with various controls"""
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Application Settings")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # General settings
        general_group = QGroupBox("General Settings")
        general_layout = QVBoxLayout(general_group)
        
        # Checkboxes
        auto_save = QCheckBox("Auto-save changes")
        auto_save.setChecked(True)
        notifications = QCheckBox("Enable notifications")
        notifications.setChecked(True)
        
        general_layout.addWidget(auto_save)
        general_layout.addWidget(notifications)
        
        # Theme selection
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Theme:"))
        
        theme_light = QRadioButton("Light")
        theme_dark = QRadioButton("Dark")
        theme_colorful = QRadioButton("Colorful")
        theme_light.setChecked(True)
        
        theme_layout.addWidget(theme_light)
        theme_layout.addWidget(theme_dark)
        theme_layout.addWidget(theme_colorful)
        theme_layout.addStretch()
        
        general_layout.addLayout(theme_layout)
        layout.addWidget(general_group)
        
        # Performance settings
        perf_group = QGroupBox("Performance Settings")
        perf_layout = QVBoxLayout(perf_group)
        
        # Sliders
        cpu_layout = QHBoxLayout()
        cpu_layout.addWidget(QLabel("CPU Usage Limit:"))
        cpu_slider = QSlider(Qt.Horizontal)
        cpu_slider.setRange(10, 100)
        cpu_slider.setValue(80)
        cpu_spinbox = QSpinBox()
        cpu_spinbox.setRange(10, 100)
        cpu_spinbox.setValue(80)
        cpu_slider.valueChanged.connect(cpu_spinbox.setValue)
        cpu_spinbox.valueChanged.connect(cpu_slider.setValue)
        
        cpu_layout.addWidget(cpu_slider)
        cpu_layout.addWidget(cpu_spinbox)
        cpu_layout.addWidget(QLabel("%"))
        
        perf_layout.addLayout(cpu_layout)
        layout.addWidget(perf_group)
        
        layout.addStretch()


class UsersDemo(QWidget):
    """Users demo with user management interface"""
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("User Management")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Action buttons
        button_layout = QHBoxLayout()
        add_user_btn = QPushButton("Add User")
        edit_user_btn = QPushButton("Edit User")
        delete_user_btn = QPushButton("Delete User")
        
        button_layout.addWidget(add_user_btn)
        button_layout.addWidget(edit_user_btn)
        button_layout.addWidget(delete_user_btn)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        # User table
        self.user_table = QTableWidget(8, 4)
        self.user_table.setHorizontalHeaderLabels(["Name", "Email", "Role", "Status"])
        
        # Sample user data
        users = [
            ("John Doe", "john@example.com", "Admin", "Active"),
            ("Jane Smith", "jane@example.com", "User", "Active"),
            ("Bob Johnson", "bob@example.com", "Manager", "Inactive"),
            ("Alice Brown", "alice@example.com", "User", "Active"),
            ("Charlie Wilson", "charlie@example.com", "User", "Active"),
            ("Diana Davis", "diana@example.com", "Manager", "Active"),
            ("Eve Anderson", "eve@example.com", "User", "Inactive"),
            ("Frank Miller", "frank@example.com", "Admin", "Active"),
        ]
        
        for row, (name, email, role, status) in enumerate(users):
            self.user_table.setItem(row, 0, QTableWidgetItem(name))
            self.user_table.setItem(row, 1, QTableWidgetItem(email))
            self.user_table.setItem(row, 2, QTableWidgetItem(role))
            self.user_table.setItem(row, 3, QTableWidgetItem(status))
            
        layout.addWidget(self.user_table)


class ReportsDemo(QWidget):
    """Reports demo with text output and export options"""
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Reports & Logs")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Report controls
        controls_layout = QHBoxLayout()
        
        report_type = QComboBox()
        report_type.addItems(["System Log", "Error Log", "User Activity", "Performance Report"])
        
        generate_btn = QPushButton("Generate Report")
        generate_btn.clicked.connect(self.generate_report)
        
        export_btn = QPushButton("Export to PDF")
        
        controls_layout.addWidget(QLabel("Report Type:"))
        controls_layout.addWidget(report_type)
        controls_layout.addWidget(generate_btn)
        controls_layout.addWidget(export_btn)
        controls_layout.addStretch()
        
        layout.addLayout(controls_layout)
        
        # Report output
        self.report_output = QTextEdit()
        self.report_output.setReadOnly(True)
        self.generate_report()  # Generate initial report
        layout.addWidget(self.report_output)
        
    def generate_report(self):
        """Generate a sample report"""
        import datetime
        
        report = f"""
SYSTEM REPORT
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
=================================================

SUMMARY:
- Total users: 1,234
- Active sessions: 89
- System uptime: 15 days, 4 hours
- Memory usage: 65%
- CPU usage: 42%

RECENT ACTIVITY:
- 2025-08-12 14:30: User login: john@example.com
- 2025-08-12 14:25: Report generated: Monthly Analytics
- 2025-08-12 14:20: System backup completed
- 2025-08-12 14:15: New user registered: alice@newuser.com
- 2025-08-12 14:10: Cache cleared automatically

PERFORMANCE METRICS:
- Response time: 245ms (avg)
- Database queries: 1,567 today
- API calls: 892 today
- Error rate: 0.02%

SYSTEM HEALTH:
✓ Database connection: OK
✓ External APIs: OK
✓ File system: OK
✓ Network connectivity: OK
⚠ Disk space: 85% used (warning threshold)

RECOMMENDATIONS:
1. Consider increasing disk storage
2. Optimize database queries for better performance
3. Schedule maintenance window for system updates
4. Review user access permissions

=================================================
Report generated successfully.
        """
        
        self.report_output.setPlainText(report.strip())
