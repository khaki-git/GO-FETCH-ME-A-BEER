import tkinter as tk

import flask

app = flask.Flask(__name__)


class WarningHandler(tk.Tk):
    def __init__(self, user_order: str):
        super().__init__()
        self.user_order = user_order
        self.title("Warning")

        # Window Style
        self.geometry("700x500")
        self.config(bg="#f8d7da")  # Light red background for warning
        self.resizable(False, False)

        # Title Label with better font and style
        self.label = tk.Label(self, text="Someone ordered!", font=('Roboto', 24, 'bold'), fg="#721c24", bg="#f8d7da")
        self.label.pack(pady=30)

        # Order Label with additional styling
        self.order = tk.Label(self, text=f"They ordered a {user_order}", font=('Roboto', 16), fg="#856404",
                              bg="#f8d7da")
        self.order.pack(pady=10)

        # Styled Close Button
        self.close_button = tk.Button(self, text="Close", font=('Roboto', 14), command=self.destroy,
                                      bg="#4CAF50", fg="white", relief="solid",
                                      width=10, height=2, bd=0,
                                      activebackground="#45a049", activeforeground="white")
        self.close_button.pack(pady=30)

        # Center window on screen
        self.eval('tk::PlaceWindow %s center' % self.winfo_toplevel())

@app.route("/cdn/<file>")
def get_file(file):
    return flask.send_file(f"./cdn/{file}")

@app.route("/api/order", methods=["POST"])
def order():
    r_json = flask.request.get_json()
    print(r_json)
    if "order" in r_json:
        WarningHandler(r_json["order"]).mainloop()
        return {}, 200
    flask.abort(400)

@app.route("/")
def index():
    return flask.send_file("./index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)