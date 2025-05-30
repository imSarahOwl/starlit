use gtk::{Application, glib};
use gtk::{ApplicationWindow, prelude::*};

const APP_ID: &str = "xyz.missowl.Starlit";

fn main() -> glib::ExitCode {
    let app = Application::builder().application_id(APP_ID).build();

    app.connect_activate(build_ui);
    app.run()
}

fn build_ui(app: &Application) {
    let window = ApplicationWindow::builder()
        .application(app)
        .title("Starlit")
        .default_height(100)
        .default_width(700)
        .resizable(false)
        .decorated(false)
        .build();

    window.set_size_request(700, 100);
    let entry = gtk::Entry::new();
    entry.connect_changed(|e| {
        finder(&e.text());
    });
    window.add(&entry);
    window.show_all();
}

fn finder(text: &str) {
    println!("{}", text)
}
