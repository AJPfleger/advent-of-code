#include <mex.h>
#include <z3++.h>
#include <iostream>

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]) {
    // P + T1*V = a + T1*u
    // P + T2*V = b + T2*v
    // P + T3*V = c + T3*w

    long long ax, ay, az, bx, by, bz, cx, cy, cz;
    int ux, uy, uz, vx, vy, vz, wx, wy, wz;

    long long *pxyz = (long long *)mxGetData(prhs[0]);
    long long *vxyz = (long long *)mxGetData(prhs[1]);

    const size_t nRows = mxGetM(prhs[0]);

    ax = pxyz[0 + nRows * 0];
    ay = pxyz[0 + nRows * 1];
    az = pxyz[0 + nRows * 2];
    bx = pxyz[1 + nRows * 0];
    by = pxyz[1 + nRows * 1];
    bz = pxyz[1 + nRows * 2];
    cx = pxyz[2 + nRows * 0];
    cy = pxyz[2 + nRows * 1];
    cz = pxyz[2 + nRows * 2];

    ux = vxyz[0 + nRows * 0];
    uy = vxyz[0 + nRows * 1];
    uz = vxyz[0 + nRows * 2];
    vx = vxyz[1 + nRows * 0];
    vy = vxyz[1 + nRows * 1];
    vz = vxyz[1 + nRows * 2];
    wx = vxyz[2 + nRows * 0];
    wy = vxyz[2 + nRows * 1];
    wz = vxyz[2 + nRows * 2];

    // Output array:
    plhs[0] = mxCreateNumericMatrix(1, 3, mxINT64_CLASS, mxREAL);
    plhs[1] = mxCreateNumericMatrix(1, 3, mxINT64_CLASS, mxREAL);

    auto P_out = (long long *)mxGetData(plhs[0]);
    auto V_out = (long long *)mxGetData(plhs[1]);

    // Z3 initialization and usage here
    z3::context ctx;

    // Create a Z3 expression for the constant
    z3::expr ax_expr = ctx.int_val(ax);
    z3::expr ay_expr = ctx.int_val(ay);
    z3::expr az_expr = ctx.int_val(az);
    z3::expr bx_expr = ctx.int_val(bx);
    z3::expr by_expr = ctx.int_val(by);
    z3::expr bz_expr = ctx.int_val(bz);
    z3::expr cx_expr = ctx.int_val(cx);
    z3::expr cy_expr = ctx.int_val(cy);
    z3::expr cz_expr = ctx.int_val(cz);

    // Create variables
    z3::expr T1 = ctx.int_const("T1");
    z3::expr T2 = ctx.int_const("T2");
    z3::expr T3 = ctx.int_const("T3");

    z3::expr Px = ctx.int_const("Px");
    z3::expr Py = ctx.int_const("Py");
    z3::expr Pz = ctx.int_const("Pz");

    z3::expr Vx = ctx.int_const("Vx");
    z3::expr Vy = ctx.int_const("Vy");
    z3::expr Vz = ctx.int_const("Vz");

    // Equations
    z3::expr equation1x = (Px + T1*Vx == ax_expr + T1*ux);
    z3::expr equation1y = (Py + T1*Vy == ay_expr + T1*uy);
    z3::expr equation1z = (Pz + T1*Vz == az_expr + T1*uz);

    z3::expr equation2x = (Px + T2*Vx == bx_expr + T2*vx);
    z3::expr equation2y = (Py + T2*Vy == by_expr + T2*vy);
    z3::expr equation2z = (Pz + T2*Vz == bz_expr + T2*vz);

    z3::expr equation3x = (Px + T3*Vx == cx_expr + T3*wx);
    z3::expr equation3y = (Py + T3*Vy == cy_expr + T3*wy);
    z3::expr equation3z = (Pz + T3*Vz == cz_expr + T3*wz);

    // Constraints
    z3::expr constraint1 = (T1 >= 0);
    z3::expr constraint2 = (T2 >= 0);
    z3::expr constraint3 = (T3 >= 0);

    z3::expr constraint12 = (T1 != T2);
    z3::expr constraint23 = (T2 != T3);
    z3::expr constraint31 = (T3 != T1);

    // Create solver
    z3::solver solver(ctx);

    // Add equations and constraints to the solver
    solver.add(equation1x);
    solver.add(equation1y);
    solver.add(equation1z);

    solver.add(equation2x);
    solver.add(equation2y);
    solver.add(equation2z);

    solver.add(equation3x);
    solver.add(equation3y);
    solver.add(equation3z);

    solver.add(constraint1);
    solver.add(constraint2);
    solver.add(constraint3);

    solver.add(constraint12);
    solver.add(constraint23);
    solver.add(constraint31);

    // Check and get the model
    z3::check_result result = solver.check();

    if (result == z3::sat) {
        z3::model model = solver.get_model();

        P_out[0] = model.eval(Px).as_int64();
        P_out[1] = model.eval(Py).as_int64();
        P_out[2] = model.eval(Pz).as_int64();

        V_out[0] = model.eval(Vx).as_int64();
        V_out[1] = model.eval(Vy).as_int64();
        V_out[2] = model.eval(Vz).as_int64();
    } else {
        std::cout << "No solution found." << std::endl;
    }
}
