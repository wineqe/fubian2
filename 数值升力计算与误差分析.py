import numpy as np
def calc_lift(U, Gamma, a, rho):
    """
    通过数值积分计算圆柱绕流的升力（修正版）
    """
    theta = np.linspace(0, 2 * np.pi, 1000)
    u_theta = (Gamma / (2 * np.pi * a)) + 2 * U * np.sin(theta)
    integrand = 0.5 * rho * a * (u_theta ** 2) * np.sin(theta)  # 修正系数和符号
    L_num = np.trapz(integrand, theta)  # 移除负号
    return L_num
# 参数设置
U = 10.0  # 来流速度 [m/s]
a = 1.0  # 圆柱半径 [m]
rho = 1.225  # 空气密度 [kg/m³]
Gamma_list = [4 * np.pi * U * a, 6 * np.pi * U * a]
# 计算并输出结果
for Gamma in Gamma_list:
    L_theory = rho * U * Gamma
    L_num = calc_lift(U, Gamma, a, rho)
    error = abs((L_num / L_theory) - 1) * 100

    print(f"环量 Γ = {Gamma / (np.pi * U * a):.1f}πUa")
    print(f"理论升力 L_theory = {L_theory:.3f} N/m")
    print(f"数值升力 L_num     = {L_num:.3f} N/m")
    print(f"相对误差 ε         = {error:.2f}%")
    print("-" * 50)