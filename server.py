from flask import Flask, jsonify
from harness.alan_harness import alan_harness
from intention.alan_intention import alan_intention

app = Flask(__name__)

@app.route('/run-attack', methods=['GET'])
def run_attack():
    harness = YourCustomHarness()
    intention = YourAttackIntention()
    prompt = intention.question_prompt

    # Assume your harness returns a string response
    response = harness.run_harness(prompt)
    return jsonify({'result': response})

if __name__ == '__main__':
    app.run(debug=True)
