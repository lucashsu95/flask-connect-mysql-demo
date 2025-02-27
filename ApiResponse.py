from flask import jsonify

class ApiResponse:
    @staticmethod
    def format_user(user):
        return {
            'id': user.id,
            'account': user.account,
            'password': user.password
        }

    @staticmethod
    def success(data):
        return jsonify({"success": True, "data": data}), 200

    @staticmethod
    def fail(message, status_code=404):
        return jsonify({"success": False, "message": message}), status_code
