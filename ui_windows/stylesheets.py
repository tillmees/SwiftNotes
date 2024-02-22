def get_stylesheet_dark():
    style_content = """
    #MainWindow {
    background-color: #1e1f22;
    }
    
    * {
        font-family: Consolas;
        letter-spacing: 0px;
    }
    
    #TopBarQWidget QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #TopBarQWidget QPushButton:hover {
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #TopBarQWidget QPushButton:pressed {
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #IconSidebarQWidget {
        background-color: #2b2d30;
        width: 50px;
    }
    
    #IconSidebarQWidget QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #IconSidebarQWidget QPushButton:hover{
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #IconSidebarQWidget QPushButton:pressed{
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #IconSidebarQWidget QFrame {
        color: #1e1f22;
    }
    
    #FullSidebarQWidget {
        background-color: #2b2d30;
        width: 250px;
    }
    
    #FullSidebarQWidget QPushButton{
        height: 30px;
        width: 30px;
        border: none;
        color: #acacac;
    }
    
    #FullSidebarQWidget QPushButton:hover{
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #FullSidebarQWidget QPushButton:pressed{
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #FullSidebarQWidget QFrame{
        color: #1e1f22;
    }
    
    #FullSidebarQWidget #label_light{
        color: #acacac;
    }
    
    #FullSidebarQWidget #label_dark{
        color: #ffffff;
    }
    
    #labelWelcome {
        font-size: 24px;
        color: rgb(200, 200, 200);
    }
    
    #labelWelcomeDrop {
        font-size: 14px;
        color: #acacac;
    }
    
    #labelCurrentProject {
        font-size: 14px;
        color: rgb(0, 0, 0);
    }
    
    #TaskPage QScrollArea {
        background-color: #2b2d30;
        border: none;
    }
    
    #labelOpenOutOf {
        color: #acacac;
    }
    
    #labelInProgressOutOf {
        color: #acacac;
    }
    
    #labelStuckTestOutOf {
        color: #acacac;
    }
    
    #labelDoneOutOf {
        color: #acacac;
    }
    
    #labelOpen {
        color: #acacac;
    }
    
    #labelInProgress {
        color: #acacac;
    }
    
    #labelStuckTest {
        color: #acacac;
    }
    
    #labelDone {
        color: #acacac;
    }
    
    #AddProjectDialog {
        background-color: #2b2d30;
    }
    
    #AddProjectDialog QLineEdit {
        border: 1px;
        background-color: #43454a;
        color: #ffffff;
    }
    
    #AddProjectDialog QPlainTextEdit {
        border: 1px;
        background-color: #43454a;
        color: #ffffff;
    }
    
    #InfoProjectDialog {
        background-color: #2b2d30;
    }
    
    #InfoProjectDialog QLabel {
        color: #ffffff;
    }
    
    #InfoProjectDialog QPlainTextEdit {
        border: 1px;
        background-color: #43454a;
        color: #ffffff;
    }
    
    #AddTaskDialog {
        background-color: #2b2d30;
    }
    
    #AddTaskDialog QLineEdit {
        border: 1px;
        background-color: #43454a;
        color: #ffffff;
    }
    
    #AddTaskDialog QPlainTextEdit {
        border: 1px;
        background-color: #43454a;
        color: #ffffff;
    }
    
    #InfoTaskDialog {
        background-color: #2b2d30;
    }
    
    #InfoTaskDialog QLabel {
        color: #ffffff;
    }
    
    #InfoTaskDialog QPlainTextEdit {
        border: 1px;
        background-color: #43454a;
        color: #ffffff;
    }
    
    #TaskWidget {
        border-radius: 5px;
    }
    
    #ProjectWidget {
        border-radius: 5px;
    }
    
    #labelTask {
        color: #000000;
        font-size: 14px;
        font-weight: bold;
    }
    
    #labelTaskCreated {
        font-size: 11px;
        color: #ffffff;
    }
    
    #TaskWidget QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #scrollAreaWidgetContentsOpen {
        background-color: #43454a;
    }
    
    #scrollAreaWidgetContentsInProgress {
        background-color: #43454a;
    }
    
    #scrollAreaWidgetContentsStuckTest {
        background-color: #43454a;
    }
    
    #scrollAreaWidgetContentsDone {
        background-color: #43454a;
    }
    
    #ProjectPage QLabel {
        color: #acacac;
    }
    
    #ProjectPage QToolButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #ProjectPage QToolButton:hover {
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #ProjectPage QToolButton:pressed {
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #ProjectPage QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #ProjectPage QPushButton:hover {
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #ProjectPage QPushButton:pressed {
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #scrollAreaWidgetContentsProjectsList {
        background-color: #43454a;
    }
    
    #ProjectPage QScrollArea {
        border: none;
    }
    """
    return style_content

def get_stylesheet_light():
    style_content = """
    #MainWindow {
    background-color: #eeeeee;
    }
    
    * {
        font-family: Consolas;
        letter-spacing: 0px;
    }
    
    #TopBarQWidget QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #TopBarQWidget QPushButton:hover {
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #TopBarQWidget QPushButton:pressed {
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #IconSidebarQWidget {
        background-color: rgb(200, 200, 200);
        width: 50px;
    }
    
    #IconSidebarQWidget QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #IconSidebarQWidget QPushButton:hover{
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #IconSidebarQWidget QPushButton:pressed{
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #IconSidebarQWidget QFrame {
        color: rgb(180, 180, 180);
    }
    
    #FullSidebarQWidget {
        background-color: rgb(200, 200, 200);
        width: 250px;
    }
    
    #FullSidebarQWidget QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #FullSidebarQWidget QPushButton:hover{
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #FullSidebarQWidget QPushButton:pressed{
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #FullSidebarQWidget QFrame {
        color: rgb(180, 180, 180);
    }
    
    
    #FullSidebarQWidget #label_light{
        color: #000000;
    }
    
    #FullSidebarQWidget #label_dark{
        color: #8a8a8a;
    }
    
    #labelWelcome {
        font-size: 24px;
        color: rgb(200, 200, 200);
    }
    
    #labelWelcomeDrop {
        font-size: 14px;
        color: rgb(30, 30, 30);
    }
    
    #labelCurrentProject {
        font-size: 14px;
        color: rgb(0, 0, 0);
    }
    
    #TaskPage QScrollArea {
        background-color: rgb(245, 245, 245);
        border: none;
    }
    
    #labelOpenOutOf {
        color: rgba(86, 101, 115, 0.5);
    }
    
    #labelInProgressOutOf {
        color: rgba(86, 101, 115, 0.5);
    }
    
    #labelStuckTestOutOf {
        color: rgba(86, 101, 115, 0.5);
    }
    
    #labelDoneOutOf {
        color: rgba(86, 101, 115, 0.5);
    }
    
    #AddProjectDialog {
        background-color: rgb(245, 245, 245);
    }
    
    #AddProjectDialog QLineEdit {
        border: none;
        background-color: #ffffff;
    }
    
    #AddProjectDialog QPlainTextEdit {
        border: none;
        background-color: #ffffff;
    }
    
    #InfoProjectDialog QPlainTextEdit {
        border: none;
        background-color: #ffffff;
    }
    
    #AddTaskDialog {
        background-color: rgb(245, 245, 245);
    }
    
    #AddTaskDialog QLineEdit {
        border: none;
        background-color: #ffffff;
    }
    
    #AddTaskDialog QPlainTextEdit {
        border: none;
        background-color: #ffffff;
    }
    
    #InfoTaskDialog QPlainTextEdit {
        border: none;
        background-color: #ffffff;
    }
    
    #TaskWidget {
        border-radius: 5px;
    }
    
    #ProjectWidget {
        border-radius: 5px;
    }
    
    #labelTask {
        font-size: 14px;
        font-weight: bold;
    }
    
    #plainTextEditTaskDescription {
        background-color: rgb(255, 180, 180);
        border: none
    }
    
    #labelTaskCreated {
        font-size: 11px;
        color: #ffffff;
    }
    
    #TaskWidget QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #scrollAreaWidgetContentsOpen {
        background-color: #ffffff;
    }
    
    #scrollAreaWidgetContentsInProgress {
        background-color: #ffffff;
    }
    
    #scrollAreaWidgetContentsStuckTest {
        background-color: #ffffff;
    }
    
    #scrollAreaWidgetContentsDone {
        background-color: #ffffff;
    }
    
    #ProjectPage QToolButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #ProjectPage QToolButton:hover {
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #ProjectPage QToolButton:pressed {
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #ProjectPage QPushButton{
        height: 30px;
        width: 30px;
        border: none;
    }
    
    #ProjectPage QPushButton:hover {
        background-color: rgba(86, 101, 115, 0.5);
    }
    
    #ProjectPage QPushButton:pressed {
        background-color: rgba(46, 61, 75, 0.5);
    }
    
    #scrollAreaWidgetContentsProjectsList {
        background-color: #ffffff;
    }
    
    #ProjectPage QScrollArea {
        border: none;
    }
    """
    return style_content

